import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QToolBar,
    QLineEdit, QPushButton, QAction, QStatusBar, QLabel, QWidget
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

class BrowserTab(QWebEngineView):
    """A single browser tab (Chromium view)."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setUrl(QUrl("https://www.google.com"))

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Chromium Browser")
        self.setGeometry(100, 100, 1024, 768)

        # Apply Bootstrap-like style sheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QToolBar {
                background-color: #ffffff;
                border-bottom: 1px solid #dee2e6;
                padding: 4px;
                spacing: 4px;
            }
            QToolButton, QPushButton {
                background-color: #f8f9fa;
                border: 1px solid #ced4da;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 14px;
            }
            QToolButton:hover, QPushButton:hover {
                background-color: #e2e6ea;
                border-color: #adb5bd;
            }
            QLineEdit {
                border: 1px solid #ced4da;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 14px;
                background-color: white;
                selection-background-color: #007bff;
            }
            QLineEdit:focus {
                border-color: #80bdff;
                outline: 0;
            }
            QTabWidget::pane {
                border: 1px solid #dee2e6;
                background: white;
            }
            QTabBar::tab {
                background: #f1f3f4;
                border: 1px solid #dee2e6;
                border-bottom: none;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                padding: 8px 12px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background: white;
                border-bottom-color: white;
            }
            QTabBar::tab:hover {
                background: #e9ecef;
            }
            QStatusBar {
                background-color: #e9ecef;
                color: #495057;
                font-size: 12px;
                border-top: 1px solid #dee2e6;
            }
        """)

        # Central tab widget
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        # Connect tab change signal after address bar is created
        self.setCentralWidget(self.tabs)

        # Create first tab
        self.add_new_tab()

        # Navigation toolbar
        nav_toolbar = QToolBar("Navigation")
        nav_toolbar.setMovable(False)
        self.addToolBar(nav_toolbar)

        # Back button
        back_btn = QAction("←", self)
        back_btn.setStatusTip("Go back")
        back_btn.triggered.connect(lambda: self.current_browser().back())
        nav_toolbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction("→", self)
        forward_btn.setStatusTip("Go forward")
        forward_btn.triggered.connect(lambda: self.current_browser().forward())
        nav_toolbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction("↻", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.current_browser().reload())
        nav_toolbar.addAction(reload_btn)

        # Home button
        home_btn = QAction("🏠", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.go_home)
        nav_toolbar.addAction(home_btn)

        # Address bar
        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText("Enter URL or search...")
        self.address_bar.returnPressed.connect(self.navigate)
        nav_toolbar.addWidget(self.address_bar)

        # Go button
        go_btn = QPushButton("Go")
        go_btn.clicked.connect(self.navigate)
        nav_toolbar.addWidget(go_btn)

        # New tab button
        new_tab_btn = QPushButton("+ New Tab")
        new_tab_btn.clicked.connect(lambda: self.add_new_tab())
        nav_toolbar.addWidget(new_tab_btn)

        # Spacer to push Gmail button to the right
        spacer = QWidget()
        spacer.setSizePolicy(spacer.sizePolicy().Expanding, spacer.sizePolicy().Preferred)
        nav_toolbar.addWidget(spacer)

        # Gmail button (opens Gmail in a new tab)
        gmail_btn = QPushButton("📧 Gmail")
        gmail_btn.clicked.connect(self.open_gmail)
        nav_toolbar.addWidget(gmail_btn)

        # Status bar
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status_label = QLabel("Ready")
        self.status.addWidget(self.status_label)

        # Connect tab change signal after address bar is created
        self.tabs.currentChanged.connect(self.tab_changed)
    def current_browser(self):
        """Return the currently visible QWebEngineView."""
        return self.tabs.currentWidget()

    def add_new_tab(self, url=None):
        """Create a new browser tab."""
        if url is None:
            url = QUrl("https://www.google.com")
        elif isinstance(url, str):
            url = QUrl(url)

        tab = BrowserTab()
        tab.setUrl(url)
        i = self.tabs.addTab(tab, "New Tab")
        self.tabs.setCurrentIndex(i)

        # Update address bar when URL changes
        tab.urlChanged.connect(lambda qurl: self.update_address_bar(qurl, tab))
        # Update tab title
        tab.titleChanged.connect(lambda title: self.tabs.setTabText(i, title[:15]))

    def close_tab(self, index):
        """Close the tab at given index."""
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            # Keep at least one tab
            self.status_label.setText("Cannot close the last tab")

    def tab_changed(self, index):
        """Update address bar when switching tabs."""
        qurl = self.current_browser().url()
        self.update_address_bar(qurl, self.current_browser())

    def update_address_bar(self, qurl, browser=None):
        """Update address bar text if the signal comes from current tab."""
        if browser == self.current_browser():
            self.address_bar.setText(qurl.toString())
            self.address_bar.setCursorPosition(0)

    def navigate(self):
        """Load the URL from address bar."""
        text = self.address_bar.text().strip()
        if not text:
            return

        # If it's a search query (no dots and not a URL), use Google
        if not text.startswith(('http://', 'https://', 'ftp://')):
            if '.' in text and not ' ' in text:
                text = 'http://' + text
            else:
                text = 'https://www.google.com/search?q=' + text.replace(' ', '+')

        qurl = QUrl(text)
        if qurl.isValid():
            self.current_browser().setUrl(qurl)
            self.status_label.setText("Loading...")

    def go_home(self):
        """Navigate to the home page (Google)."""
        self.current_browser().setUrl(QUrl("https://www.google.com"))

    def open_gmail(self):
        """Open Gmail in a new tab."""
        self.add_new_tab("https://mail.google.com")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Python Chromium Browser")
    window = Browser()
    window.show()
    sys.exit(app.exec_())