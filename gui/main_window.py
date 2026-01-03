import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QStackedWidget, 
                             QFrame, QTextEdit)
from PyQt6.QtCore import Qt, QSize, QThread, pyqtSignal
from PyQt6.QtGui import QIcon
import qtawesome as qta
import qdarktheme

# Add parent dir to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai.model import HearthstoneModel
from gui.tabs.training_tab import TrainingTab
from gui.tabs.spy_tab import SpyTab
from training.trainer import Trainer

class TrainingThread(QThread):
    log_signal = pyqtSignal(str)
    
    def run(self):
        # Redirect stdout
        class Logger:
            def __init__(self, signal):
                self.signal = signal
            def write(self, text):
                if text.strip():
                    self.signal.emit(text)
            def flush(self):
                pass
        
        # Backup original sys.stdout
        original_stdout = sys.stdout
        sys.stdout = Logger(self.log_signal)
        
        try:
            trainer = Trainer()
            trainer.train()
        except Exception as e:
            self.log_signal.emit(f"ERROR: {e}")
        finally:
            sys.stdout = original_stdout

class SideBarButton(QPushButton):
    def __init__(self, icon_name, text, parent=None):
        super().__init__(text, parent)
        self.setIcon(qta.icon(icon_name, color="#94a3b8"))
        self.setIconSize(QSize(20, 20))
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty("active", "false")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HearthstoneOne — AI Dashboard")
        self.resize(1100, 850)
        
        # Load Styles
        self.load_stylesheet()
        
        # Central Widget
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QHBoxLayout(self.main_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        # 1. Sidebar
        self.setup_sidebar()
        
        # 2. Main Content Area
        self.content_container = QWidget()
        self.container_layout = QVBoxLayout(self.content_container)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(0)
        self.layout.addWidget(self.content_container)
        
        # 2.1 Header
        self.setup_header()
        
        # 2.2 Stacked Pages
        self.pages = QStackedWidget()
        self.container_layout.addWidget(self.pages)
        
        # 2.3 Terminal Log
        self.console = QTextEdit()
        self.console.setObjectName("console")
        self.console.setReadOnly(True)
        self.console.setFixedHeight(180)
        self.console.setPlaceholderText("Les logs système s'afficheront ici...")
        self.container_layout.addWidget(self.console)
        
        # Initialize Pages
        self.init_pages()
        
        # Connections
        self.training_thread = TrainingThread()
        self.training_thread.log_signal.connect(self.append_log)
        self.training_page.btn_start.clicked.connect(self.start_training)
        
        # Default Page
        self.switch_page(0)

    def append_log(self, text):
        self.console.append(text)

    def start_training(self):
        self.status_label.setText("● ENTRAÎNEMENT ACTIF")
        self.status_label.setStyleSheet("color: #10b981; font-weight: bold; margin-right: 15px;")
        self.training_page.btn_start.setEnabled(False)
        self.training_page.btn_stop.setEnabled(True)
        self.training_thread.start()

    def load_stylesheet(self):
        css_path = os.path.join(os.path.dirname(__file__), "style.css")
        if os.path.exists(css_path):
            with open(css_path, "r") as f:
                self.setStyleSheet(f.read())

    def setup_sidebar(self):
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(0, 20, 0, 20)
        self.sidebar_layout.setSpacing(5)
        
        # Buttons
        self.btn_train = SideBarButton("fa.rocket", "Entraînement")
        self.btn_spy = SideBarButton("fa.eye", "Mode Espion")
        self.btn_decks = SideBarButton("fa.book", "Meta Decks")
        self.btn_stats = SideBarButton("fa.line-chart", "Analyses")
        self.btn_settings = SideBarButton("fa.cog", "Réglages")
        
        self.btn_train.clicked.connect(lambda: self.switch_page(0))
        self.btn_spy.clicked.connect(lambda: self.switch_page(1))
        self.btn_decks.clicked.connect(lambda: self.switch_page(2))
        self.btn_stats.clicked.connect(lambda: self.switch_page(3))
        self.btn_settings.clicked.connect(lambda: self.switch_page(4))
        
        self.sidebar_layout.addWidget(self.btn_train)
        self.sidebar_layout.addWidget(self.btn_spy)
        self.sidebar_layout.addWidget(self.btn_decks)
        self.sidebar_layout.addWidget(self.btn_stats)
        self.sidebar_layout.addStretch()
        self.sidebar_layout.addWidget(self.btn_settings)
        
        self.layout.addWidget(self.sidebar)
        
        self.nav_buttons = [self.btn_train, self.btn_spy, self.btn_decks, self.btn_stats, self.btn_settings]

    def setup_header(self):
        self.header = QFrame()
        self.header.setObjectName("header")
        self.header.setFixedHeight(60)
        header_layout = QHBoxLayout(self.header)
        
        logo = QLabel("HEARTHSTONE ONE")
        logo.setObjectName("logo_label")
        header_layout.addWidget(logo)
        header_layout.addStretch()
        
        # Status Badge
        self.status_label = QLabel("● SYSTÈME PRÊT")
        self.status_label.setStyleSheet("color: #94a3b8; font-weight: bold; margin-right: 15px;")
        header_layout.addWidget(self.status_label)
        
        self.container_layout.addWidget(self.header)

    def init_pages(self):
        # 0. Training Page
        self.training_page = TrainingTab()
        self.pages.addWidget(self.training_page)
        
        # 1. Spy Mode Page
        self.spy_page = SpyTab()
        self.pages.addWidget(self.spy_page)
        
        # Others (Placeholders)
        for name in ["Meta Decks", "Analytics", "Settings"]:
            page = QWidget()
            layout = QVBoxLayout(page)
            title = QLabel(f"{name} Control Center")
            title.setObjectName("title_label")
            layout.addWidget(title)
            layout.addStretch()
            self.pages.addWidget(page)

    def switch_page(self, index):
        self.pages.setCurrentIndex(index)
        for i, btn in enumerate(self.nav_buttons):
            btn.setProperty("active", "true" if i == index else "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Apply global dark theme for standard widgets (buttons, combo boxes etc)
    app.setStyleSheet(qdarktheme.load_stylesheet())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
