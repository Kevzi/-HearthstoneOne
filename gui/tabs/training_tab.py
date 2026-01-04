from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QFrame, 
                             QLabel, QPushButton, QProgressBar, QApplication)
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt6.QtGui import QPixmap, QColor, QFont
import os

class TrainingTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(30, 30, 30, 30)
        self.layout.setSpacing(0)
        
        # 1. Hero Section (Branding)
        hero_layout = QVBoxLayout()
        hero_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Logo Section (Hero)
        self.logo_label = QLabel()
        logo_path = os.path.join("gui", "assets", "logo.png")
        if os.path.exists(logo_path):
            pix = QPixmap(logo_path).scaled(160, 160, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.logo_label.setPixmap(pix)
        else:
            self.logo_label.setText("💠")
            self.logo_label.setStyleSheet("font-size: 120px; color: #0ea5e9;")
        
        hero_layout.addWidget(self.logo_label, 0, Qt.AlignmentFlag.AlignCenter)
        
        hero_layout.addWidget(self.logo_label, 0, Qt.AlignmentFlag.AlignCenter)
        
        # Dashboard Info (Clean & Modern)
        self.version_label = QLabel("NEURAL CORE ENGINE v2.5.0")
        self.version_label.setStyleSheet("font-size: 9px; color: #475569; font-weight: bold; margin-top: 10px; letter-spacing: 2px;")
        hero_layout.addWidget(self.version_label, 0, Qt.AlignmentFlag.AlignCenter)
        
        self.status_tag = QLabel("CONNECTED · OPTIMIZED")
        self.status_tag.setStyleSheet("""
            background-color: rgba(16, 185, 129, 0.1); 
            color: #10b981; 
            padding: 4px 12px; 
            border-radius: 10px; 
            font-size: 9px; 
            font-weight: bold; 
            margin-top: 12px; 
            margin-bottom: 20px;
        """)
        hero_layout.addWidget(self.status_tag, 0, Qt.AlignmentFlag.AlignCenter)
        
        self.layout.addLayout(hero_layout)
        
        # 2. Main Dashboard Card (Glassmorphism)
        self.dash_card = QFrame()
        self.dash_card.setObjectName("dash_card")
        self.dash_card.setProperty("class", "glass-card")
        self.dash_card.setMinimumHeight(240)
        self.dash_layout = QVBoxLayout(self.dash_card)
        self.dash_layout.setContentsMargins(30, 25, 30, 25)
        self.dash_layout.setSpacing(25)
        
        # Stats Row
        stats_row = QHBoxLayout()
        self.stat_iter = self.create_mini_stat("ITERATION", "0")
        self.stat_status = self.create_mini_stat("SYSTEM STATUS", "READY")
        self.stat_wr = self.create_mini_stat("AGENT WIN RATE", "--%")
        
        stats_row.addWidget(self.stat_iter)
        stats_row.addStretch()
        stats_row.addWidget(self.stat_status)
        stats_row.addStretch()
        stats_row.addWidget(self.stat_wr)
        
        self.dash_layout.addLayout(stats_row)
        
        # Action Row
        action_layout = QHBoxLayout()
        action_layout.setSpacing(20)
        
        self.btn_start = QPushButton("INITIATE NEURAL LINK")
        self.btn_start.setObjectName("neural-btn")
        self.btn_start.setFixedSize(260, 48)
        self.btn_start.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btn_stop = QPushButton("STOP")
        self.btn_stop.setObjectName("stop-btn")
        self.btn_stop.setFixedSize(110, 48)
        self.btn_stop.setEnabled(False)
        self.btn_stop.setCursor(Qt.CursorShape.PointingHandCursor)
        
        action_layout.addStretch()
        action_layout.addWidget(self.btn_start)
        action_layout.addWidget(self.btn_stop)
        action_layout.addStretch()
        
        self.dash_layout.addLayout(action_layout)
        
        self.layout.addWidget(self.dash_card)
        self.layout.addStretch()

    def create_mini_stat(self, label, value):
        w = QWidget()
        l = QVBoxLayout(w)
        l.setSpacing(2)
        l.setContentsMargins(0,0,0,0)
        l.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        lbl = QLabel(label)
        lbl.setStyleSheet("color: #64748b; font-size: 10px; font-weight: bold;")
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
        
        if hasattr(self, 'stat_iter'):
            self.stat_iter.val_label.setText(str(iteration))
        if hasattr(self, 'stat_wr'):
            self.stat_wr.val_label.setText(f"{wr_p2:.1f}%")
        if hasattr(self, 'stat_status'):
            self.stat_status.val_label.setText("LEARNING")
            self.stat_status.val_label.setStyleSheet("color: #3b82f6; font-size: 18px; font-weight: bold;")
        
        if hasattr(self, 'version_label'):
            self.version_label.setText(f"PROCESSING NEURAL BATCH {iteration}")
            self.version_label.setStyleSheet("color: #3b82f6; font-size: 9px; font-weight: bold; letter-spacing: 2px;")
