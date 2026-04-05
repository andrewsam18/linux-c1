import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
import qtawesome as qta
from adblockparser import AdblockRules

HOME = "https://www.google.com"


# ---------- Ad Blocker ----------
class AdBlockerInterceptor(QWebEngineUrlRequestInterceptor):

    def __init__(self):
        super().__init__()
        self.rules = None

        try:
            with open("easylist.txt", encoding="utf8") as f:
                raw_rules = f.readlines()

            self.rules = AdblockRules(raw_rules)
            print("AdBlocker Loaded:", len(raw_rules), "rules")

        except FileNotFoundError:
            print("easylist.txt not found → Adblock disabled")

        except Exception as e:
            print("Adblock error:", e)

    def interceptRequest(self, info):

        if self.rules:

            url = info.requestUrl().toString()

            if self.rules.should_block(url):
                print("Blocked:", url)
                info.block(True)


# ---------- Browser Window ----------
class Browser(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Don Browser")
        self.showMaximized()

        # Setup Adblock
        self.interceptor = AdBlockerInterceptor()
        QWebEngineProfile.defaultProfile().setRequestInterceptor(self.interceptor)

        # Browser view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(HOME))

        self.setCentralWidget(self.browser)

        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction(qta.icon('fa5s.arrow-left'), "Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction(qta.icon('fa5s.arrow-right'), "Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(qta.icon('fa5s.sync'), "Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(qta.icon('fa5s.home'), "Home", self)
        home_btn.triggered.connect(self.go_home)
        navbar.addAction(home_btn)

        navbar.addSeparator()

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
import qtawesome as qta
from adblockparser import AdblockRules

HOME = "https://www.google.com"

class AdBlockerInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self):
        super().__init__()
        self.enabled = True          # Ad blocking is ON by default
        self.rules = None
        try:
            with open("easylist.txt") as f:
                raw_rules = f.readlines()
            self.rules = AdblockRules(raw_rules)
            print(f"AdBlocker: Loaded {len(raw_rules)} rules.")
        except FileNotFoundError:
            print("AdBlocker: easylist.txt not found. Ad-blocking disabled.")
        except Exception as e:
            print(f"AdBlocker: Error loading rules - {e}")

    def set_enabled(self, enabled):
        self.enabled = enabled
        print(f"AdBlocker: {'Enabled' if enabled else 'Disabled'}")

    def interceptRequest(self, info):
        # Only block if we have rules and blocking is enabled
        if self.rules and self.enabled:
            url = info.requestUrl().toString()
            if self.rules.should_block(url):
                print(f"AdBlocker: Blocked {url}")
                info.block(True)


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Don Browser")
        self.showMaximized()

        # Setup ad blocker interceptor
        self.interceptor = AdBlockerInterceptor()
        QWebEngineProfile.defaultProfile().setRequestInterceptor(self.interceptor)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(HOME))
        self.setCentralWidget(self.browser)

        # Create toolbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Navigation buttons
        back_btn = QAction(qta.icon('fa5s.arrow-left'), "Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction(qta.icon('fa5s.arrow-right'), "Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(qta.icon('fa5s.sync'), "Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(qta.icon('fa5s.home'), "Home", self)
        home_btn.triggered.connect(self.go_home)
        navbar.addAction(home_btn)

        # --- Ad Block Toggle Button ---
        self.adblock_action = QAction(qta.icon('fa5s.shield-alt'), "Ad Block", self)
        self.adblock_action.setCheckable(True)
        self.adblock_action.setChecked(True)          # start enabled
        self.adblock_action.toggled.connect(self.toggle_adblock)

        # If rules failed to load, disable the toggle and show tooltip
        if self.interceptor.rules is None:
            self.adblock_action.setEnabled(False)
            self.adblock_action.setToolTip("Ad blocking unavailable (easylist.txt missing or invalid)")
        else:
            self.adblock_action.setToolTip("Toggle ad blocking")

        navbar.addAction(self.adblock_action)
        navbar.addSeparator()

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        search_btn = QAction(qta.icon('fa5s.search'), "Go", self)
        search_btn.triggered.connect(self.navigate_to_url)
        navbar.addAction(search_btn)

        # Connect URL change to update address bar
        self.browser.urlChanged.connect(self.update_url)

    def toggle_adblock(self, checked):
        """Called when the ad block button is toggled."""
        self.interceptor.set_enabled(checked)
        # Change icon to give visual feedback
        if checked:
            self.adblock_action.setIcon(qta.icon('fa5s.shield-alt'))
        else:
            self.adblock_action.setIcon(qta.icon('fa5s.ban'))   # use ban symbol when off

    def go_home(self):
        self.browser.setUrl(QUrl(HOME))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if "http" not in url:
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())