import sys, os
from urllib.parse import urlparse
from PyQt5.QtCore import QUrl, Qt, QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor

HOME = "https://www.google.com"

# ---------------- AdBlock ----------------
AD_PATTERNS = [
    "doubleclick.net",
    "googlesyndication.com",
    "googleadservices.com",
    "adservice.google.com",
    "adnxs.com",
    "taboola.com",
    "outbrain.com"
]


class AdBlocker(QWebEngineUrlRequestInterceptor):

    def __init__(self):
        super().__init__()
        self.enabled = True

    def interceptRequest(self, info):
        if not self.enabled:
            return

        url = info.requestUrl().toString().lower()

        for pattern in AD_PATTERNS:
            if pattern in url:
                info.block(True)
                return


# ---------------- Download Window ----------------
class DownloadWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Downloads")
        self.resize(400,300)

        self.list = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.list)

        self.setLayout(layout)

    def add(self, text):
        self.list.addItem(text)


# ---------------- History Window ----------------
class HistoryWindow(QDialog):

    def __init__(self, open_callback):
        super().__init__()

        self.setWindowTitle("History")
        self.resize(400,300)

        self.list = QListWidget()
        self.list.itemClicked.connect(lambda x: open_callback(x.text()))

        layout = QVBoxLayout()
        layout.addWidget(self.list)

        self.setLayout(layout)

    def add(self, url):
        self.list.addItem(url)


# ---------------- Browser ----------------
class Browser(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Don Browser")
        self.resize(1200,800)

        self.dark_mode = False
        self.mobile_mode = False

        self.profile = QWebEngineProfile.defaultProfile()

        self.adblocker = AdBlocker()
        self.profile.setRequestInterceptor(self.adblocker)

        self.profile.downloadRequested.connect(self.download)

        self.downloads = DownloadWindow()
        self.history_win = HistoryWindow(self.add_tab)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_url)

        self.setCentralWidget(self.tabs)

        # Address bar
        self.address = QLineEdit()
        self.address.returnPressed.connect(self.navigate)

        # Toolbar
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        toolbar.addAction("◀", lambda: self.current().back())
        toolbar.addAction("▶", lambda: self.current().forward())
        toolbar.addAction("⟳", lambda: self.current().reload())
        toolbar.addAction("🏠", self.open_home)

        toolbar.addWidget(self.address)

        toolbar.addAction("⭐", self.add_bookmark)
        toolbar.addAction("📥", self.downloads.show)
        toolbar.addAction("🕓", self.history_win.show)
        toolbar.addAction("🌙", self.toggle_dark)

        toolbar.addAction("+", lambda: self.add_tab())

        # bookmarks
        self.bookmarks = QListWidget()
        self.bookmarks.itemClicked.connect(lambda x: self.add_tab(x.text()))

        dock = QDockWidget("Bookmarks")
        dock.setWidget(self.bookmarks)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        self.add_tab(HOME)

    # -------- Tabs --------
    def add_tab(self, url=None):

        browser = QWebEngineView()

        if url:
            browser.setUrl(QUrl(url))
        else:
            browser.setUrl(QUrl(HOME))

        i = self.tabs.addTab(browser, "New Tab")
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda q, b=browser: self.update_url(q,b))
        browser.loadFinished.connect(lambda _, b=browser: self.update_title(b))
        browser.urlChanged.connect(lambda q: self.history_win.add(q.toString()))

    def close_tab(self, i):

        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(i)

    def current(self):
        return self.tabs.currentWidget()

    # -------- Navigation --------
    def navigate(self):

        text = self.address.text()

        if "://" not in text:
            text = "https://www.google.com/search?q=" + text

        self.current().setUrl(QUrl(text))

    def update_url(self, q=None, browser=None):

        if browser != self.current():
            return

        self.address.setText(q.toString())

    def update_title(self, browser):

        i = self.tabs.indexOf(browser)
        self.tabs.setTabText(i, browser.page().title())

    def open_home(self):
        self.current().setUrl(QUrl(HOME))

    # -------- Bookmark --------
    def add_bookmark(self):

        url = self.current().url().toString()
        self.bookmarks.addItem(url)

    # -------- Downloads --------
    def download(self, item):

        path, _ = QFileDialog.getSaveFileName(self, "Save File", item.path())

        if path:
            item.setPath(path)
            item.accept()
            self.downloads.add(path)

    # -------- Dark Mode --------
    def toggle_dark(self):

        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            self.setStyleSheet("background:#1e1e1e;color:white")
        else:
            self.setStyleSheet("")

# ---------------- Run ----------------
app = QApplication(sys.argv)

app.setApplicationName("Don Browser")

window = Browser()
window.show()

sys.exit(app.exec_())