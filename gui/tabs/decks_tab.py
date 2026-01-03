from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QFrame, 
                             QLabel, QPushButton, QScrollArea, QListWidget, QListWidgetItem)
from PyQt6.QtCore import Qt
import qtawesome as qta
from simulator.deck_generator import META_DECK_CODES

class DecksTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        header = QHBoxLayout()
        title = QLabel("BIBLIOTHÈQUE DE META DECKS")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        header.addWidget(title)
        header.addStretch()
        
        btn_refresh = QPushButton(" Actualiser")
        btn_refresh.setIcon(qta.icon("fa5s.sync", color="white"))
        btn_refresh.setStyleSheet("background-color: #334155; padding: 5px 15px; border-radius: 5px;")
        header.addWidget(btn_refresh)
        
        self.layout.addLayout(header)
        
        # Description
        desc = QLabel("Voici les decks utilisés par l'IA pour son entraînement. Ces listes proviennent de HSGuru (Janvier 2026).")
        desc.setStyleSheet("color: #94a3b8; margin-bottom: 10px;")
        self.layout.addWidget(desc)
        
        # Scroll Area for Decks
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: transparent; border: none;")
        
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        self.grid_layout = QVBoxLayout(container)
        self.grid_layout.setSpacing(10)
        
        self.refresh_decks()
        
        scroll.setWidget(container)
        self.layout.addWidget(scroll)

    def refresh_decks(self):
        # Clear existing
        while self.grid_layout.count():
            child = self.grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
                
        # Group by class
        by_class = {}
        for code, (cls, name) in META_DECK_CODES.items():
            if cls not in by_class:
                by_class[cls] = []
            by_class[cls].append((name, code))
            
        for cls in sorted(by_class.keys()):
            # Class Header
            cls_label = QLabel(cls)
            cls_label.setStyleSheet(f"font-weight: bold; color: {self.get_class_color(cls)}; font-size: 14px; margin-top: 10px;")
            self.grid_layout.addWidget(cls_label)
            
            for name, code in by_class[cls]:
                card = QFrame()
                card.setProperty("class", "card")
                card.setFixedHeight(60)
                card_layout = QHBoxLayout(card)
                card_layout.setContentsMargins(15, 0, 15, 0)
                
                # Icon
                icon_label = QLabel()
                icon_label.setPixmap(qta.icon("fa5s.bookmark", color=self.get_class_color(cls)).pixmap(24, 24))
                card_layout.addWidget(icon_label)
                
                # Name
                name_label = QLabel(name)
                name_label.setStyleSheet("font-weight: 600; font-size: 13px;")
                card_layout.addWidget(name_label)
                
                card_layout.addStretch()
                
                # Actions
                btn_view = QPushButton("Voir Liste")
                btn_view.setStyleSheet("background-color: #334155; border-radius: 4px; padding: 4px 10px; font-size: 11px;")
                card_layout.addWidget(btn_view)
                
                self.grid_layout.addWidget(card)
        
        self.grid_layout.addStretch()

    def get_class_color(self, cls):
        colors = {
            "MAGE": "#3b82f6",
            "WARRIOR": "#ef4444",
            "ROGUE": "#f59e0b",
            "DRUID": "#10b981",
            "PALADIN": "#fbbf24",
            "PRIEST": "#f1f5f9",
            "HUNTER": "#22c55e",
            "WARLOCK": "#a855f7",
            "SHAMAN": "#2563eb",
            "DEMONHUNTER": "#8b5cf6",
            "DEATHKNIGHT": "#14b8a6"
        }
        return colors.get(cls.upper(), "#94a3b8")
