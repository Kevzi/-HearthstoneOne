from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QFrame, 
                             QLabel, QPushButton, QProgressBar, QApplication)
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt6.QtGui import QPixmap, QColor, QFont
import os

class TrainingTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(60, 80, 60, 60)
        self.layout.setSpacing(40)
        
        # 1. Main Branding (Minimalist)
        brand_layout = QVBoxLayout()
        brand_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.logo_label = QLabel()
        logo_path = os.path.join("gui", "assets", "logo.png")
        if os.path.exists(logo_path):
            pix = QPixmap(logo_path).scaled(180, 180, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.logo_label.setPixmap(pix)
        else:
            self.logo_label.setText("💠")
            self.logo_label.setStyleSheet("font-size: 100px; color: #22d3ee;")
            
        brand_layout.addWidget(self.logo_label, 0, Qt.AlignmentFlag.AlignCenter)
        
        self.title = QLabel("DEEPMANA")
        self.title.setStyleSheet("""
            font-size: 64px; 
            font-weight: 900; 
            color: #ffffff; 
            letter-spacing: 16px; 
            margin-top: 20px;
            background: transparent;
        """)
        brand_layout.addWidget(self.title, 0, Qt.AlignmentFlag.AlignCenter)
        
        self.subtitle = QLabel("NEURAL CORE: READY")
        self.subtitle.setStyleSheet("font-size: 12px; color: #475569; font-weight: bold; letter-spacing: 4px; margin-top: -10px;")
        brand_layout.addWidget(self.subtitle, 0, Qt.AlignmentFlag.AlignCenter)
        
        self.layout.addLayout(brand_layout)
        self.layout.addStretch()
        
        # 2. Controls
        btn_layout = QVBoxLayout()
        btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.btn_start = QPushButton("INITIATE NEURAL LINK")
        self.btn_start.setFixedSize(320, 60)
        self.btn_start.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_start.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #22d3ee;
                font-size: 15px;
                font-weight: bold;
                border: 2px solid #22d3ee;
                border-radius: 30px;
                letter-spacing: 3px;
            }
            QPushButton:hover {
                background: #22d3ee;
                color: #0f172a;
            }
            QPushButton:disabled {
                border-color: #1e293b;
                color: #475569;
            }
        """)
        
        self.btn_stop = QPushButton("TERMINATE")
        self.btn_stop.setFixedSize(320, 60)
        self.btn_stop.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_stop.setEnabled(False)
        self.btn_stop.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #ef4444;
                font-size: 14px;
                font-weight: bold;
                border: 1px solid #ef4444;
                border-radius: 30px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background: rgba(239, 68, 68, 0.1);
            }
        """)
        
        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)
        self.layout.addLayout(btn_layout)
        
        self.layout.addStretch()
        
        # 3. Footer Stats (Ultra Minimalist)
        stats_layout = QHBoxLayout()
        stats_layout.setContentsMargins(20, 0, 20, 0)
        
        self.stat_iter = self.create_mini_stat("ITERATION", "0")
        self.stat_wr = self.create_mini_stat("WIN RATE", "--%")
        self.stat_status = self.create_mini_stat("STATUS", "IDLE")
        
        stats_layout.addWidget(self.stat_iter)
        stats_layout.addStretch()
        stats_layout.addWidget(self.stat_status)
        stats_layout.addStretch()
        stats_layout.addWidget(self.stat_wr)
        
        self.layout.addLayout(stats_layout)

    def create_mini_stat(self, label, value):
        w = QWidget()
        l = QVBoxLayout(w)
        l.setSpacing(2)
        l.setContentsMargins(0,0,0,0)
        l.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        lbl = QLabel(label)
        lbl.setStyleSheet("color: #64748b; font-size: 10px; font-weight: bold; letter-spacing: 1px;")
        val = QLabel(value)
        val.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        
        l.addWidget(lbl)
        l.addWidget(val)
        
        w.val_label = val # Store ref
        return w

    def update_data(self, stats):
        iteration = stats.get("iteration", 0)
        winners = stats.get("winners", {})
        total_games = sum(winners.values())
        wr_p2 = (winners.get(2, 0) / total_games * 100) if total_games > 0 else 0
        
        self.stat_iter.val_label.setText(str(iteration))
        self.stat_wr.val_label.setText(f"{wr_p2:.1f}%")
        self.stat_status.val_label.setText("LEARNING")
        self.stat_status.val_label.setStyleSheet("color: #00ffff; font-size: 18px; font-weight: bold;")
        
        self.subtitle.setText(f"PROCESSING BATCH {iteration}...")
