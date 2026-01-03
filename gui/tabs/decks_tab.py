from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, 
    QListWidget, QListWidgetItem, QTextEdit, QMessageBox, QDialog,
    QScrollArea, QFrame, QApplication
)
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt, QTimer
import sys
import os

from simulator.deck_generator import DeckGenerator
from simulator.card_loader import CardDatabase

class DecksTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QHBoxLayout(self)
        
        # Left: List of Decks
        left_panel = QFrame()
        left_layout = QVBoxLayout(left_panel)
        
        title = QLabel("Meta Decks (Standard)")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #cbd5e1;")
        left_layout.addWidget(title)
        
        self.deck_list = QListWidget()
        self.deck_list.setStyleSheet("""
            QListWidget {
                background-color: #1e293b;
                color: #e2e8f0;
                border: 1px solid #334155;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 10px;
            }
            QListWidget::item:selected {
                background-color: #3b82f6;
            }
        """)
        left_layout.addWidget(self.deck_list)
        
        btn_layout = QHBoxLayout()
        refresh_btn = QPushButton("Refresh List")
        refresh_btn.clicked.connect(self.load_decks)
        view_btn = QPushButton("View Deck List")
        view_btn.clicked.connect(self.view_selected_deck)
        
        btn_layout.addWidget(refresh_btn)
        btn_layout.addWidget(view_btn)
        left_layout.addLayout(btn_layout)
        
        layout.addWidget(left_panel, 1) # Stretch 1
        
        # Load decks on start
        self.meta_decks = {} # Store loaded decks locally: name -> code
        self.load_decks()
        
    def load_decks(self):
        self.deck_list.clear()
        self.meta_decks = {}
        
        # Load from JSON via Generator
        try:
            decks_map = DeckGenerator._load_meta_decks()
        except Exception:
            self.deck_list.addItem("Error loading deck generator.")
            return
        
        if not decks_map:
            self.deck_list.addItem("No decks found or error loading JSON.")
            return

        # Group by Class for nicer display
        # New format: decks_map is now a list of (class_name, deck_name, deck_data)
        grouped = {}
        for cls_name, deck_name, deck_data in decks_map:
            if cls_name not in grouped: grouped[cls_name] = []
            grouped[cls_name].append((deck_name, deck_data))
            
        for cls_name in sorted(grouped.keys()):
            for deck_name, deck_data in grouped[cls_name]:
                display_name = f"[{cls_name}] {deck_name}"
                item = QListWidgetItem(display_name)
                # Store deck_data (can be code string or cards list)
                self.meta_decks[display_name] = deck_data
                self.deck_list.addItem(item)
                
    def view_selected_deck(self):
        current_item = self.deck_list.currentItem()
        if not current_item:
            return
            
        display_name = current_item.text()
        code = self.meta_decks.get(display_name)
        
        if code:
            self.show_deck_list(display_name, code)
            
    def show_deck_list(self, name, code):
        from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
        from simulator.enums import Rarity

        dialog = QDialog(self)
        dialog.setWindowTitle(f"Deck: {name}")
        dialog.resize(500, 700)
        dialog.setStyleSheet("background-color: #0f172a; color: white;")
        
        layout = QVBoxLayout(dialog)
        
        # Header
        header = QLabel(name)
        header.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 15px; color: #60a5fa;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)
        
        # Table
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Cost", "Name", "Qty"])
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        table.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
        table.setShowGrid(False)
        table.setStyleSheet("""
            QTableWidget {
                background-color: #1e293b;
                border: 1px solid #334155;
                font-size: 14px;
                gridline-color: #334155;
            }
            QHeaderView::section {
                background-color: #334155;
                color: #e2e8f0;
                padding: 6px;
                font-weight: bold;
                border: none;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #334155;
            }
        """)
        layout.addWidget(table)
        
        # Decode and Populate - handle both formats
        try:
            if isinstance(code, list):
                # Direct card IDs format
                card_ids = code
            else:
                # Deckstring format
                card_ids = DeckGenerator.decode_deck_string(code)
        except Exception as e:
            card_ids = []
            
        if card_ids:
            # Count
            counts = {}
            for cid in card_ids: counts[cid] = counts.get(cid, 0) + 1
            
            # Fetch Data
            db = CardDatabase.get_instance()
            if not db._loaded: db.load()
            
            rows = []
            for cid, qty in counts.items():
                card = db.get_card(cid)
                if card:
                    rows.append({
                        "cost": card.cost,
                        "name": card.name,
                        "qty": qty,
                        "rarity": card.rarity
                    })
                else:
                    # Fallback for unknown
                    rows.append({
                        "cost": 0,
                        "name": f"Unknown ({cid})",
                        "qty": qty,
                        "rarity": 0 # COMMON
                    })
            
            # Sort by Cost then Name
            rows.sort(key=lambda x: (x['cost'], x['name']))
            
            table.setRowCount(len(rows))
            
            # Rarity Colors
            rarity_colors = {
                1: "#d1d5db", # COMMON (Gray)
                2: "#ffffff", # FREE (White)
                3: "#3b82f6", # RARE (Blue)
                4: "#a855f7", # EPIC (Purple)
                5: "#f59e0b", # LEGENDARY (Orange)
            }
            
            for i, row in enumerate(rows):
                # Cost
                cost_item = QTableWidgetItem(str(row['cost']))
                cost_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                cost_item.setForeground(Qt.GlobalColor.cyan) # Mana color
                
                # Name
                name_item = QTableWidgetItem(row['name'])
                rarity_col = rarity_colors.get(int(row.get('rarity', 1)), "#d1d5db")
                name_item.setForeground(QColor(rarity_col))
                font = name_item.font()
                if int(row.get('rarity', 0)) == 5:
                    font.setBold(True)
                name_item.setFont(font)
                
                # Qty
                qty_val = row['qty']
                qty_str = f"x{qty_val}"
                if int(row.get('rarity', 0)) == 5: # Legendaries are unique usually (except accidental dupes)
                     qty_str = "★" # Star for legendary
                
                qty_item = QTableWidgetItem(qty_str)
                qty_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                
                table.setItem(i, 0, cost_item)
                table.setItem(i, 1, name_item)
                table.setItem(i, 2, qty_item)
                
        else:
            table.setRowCount(1)
            table.setItem(0, 1, QTableWidgetItem("Error decoding deck code."))

        # Footer Actions
        btn_box = QHBoxLayout()
        copy_btn = QPushButton("Copy Code")
        copy_btn.clicked.connect(lambda: QApplication.clipboard().setText(code)) # Need QApplication import
        copy_btn.setStyleSheet("background-color: #475569;")
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        close_btn.setStyleSheet("background-color: #3b82f6; font-weight: bold;")
        
        btn_box.addWidget(copy_btn)
        btn_box.addWidget(close_btn)
        layout.addLayout(btn_box)
        
        dialog.exec()
