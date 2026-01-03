import sys
import math
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QFrame
from PyQt6.QtGui import QFont, QColor, QPalette, QPainter, QPen, QPolygonF, QLinearGradient, QRadialGradient, QBrush
from PyQt6.QtCore import Qt, QTimer, QPointF, QRectF

class OverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HearthstoneOne AI Overlay")
        
        # === ANIMATION STATE ===
        self.anim_tick = 0
        self.anim_timer = QTimer(self)
        self.anim_timer.timeout.connect(self._animate)
        self.anim_timer.start(33)  # ~30 FPS
        
        # === GAME STATE ===
        self.arrow_start = None
        self.arrow_end = None
        self.highlight_pos = None
        
        # === WINDOW CONFIG ===
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        
        # Full screen coverage
        if QApplication.primaryScreen():
            screen_geo = QApplication.primaryScreen().geometry()
            self.setGeometry(screen_geo)
        else:
            self.setGeometry(0, 0, 1920, 1080)

        # === UI LAYOUT (Glassmorphism) ===
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(10)
        
        # Container for labels to create glass effect
        self.panel = QFrame()
        self.panel.setFixedWidth(400)
        self.panel.setStyleSheet("""
            QFrame {
                background-color: rgba(15, 23, 42, 180);
                border: 1px solid rgba(255, 255, 255, 30);
                border-radius: 15px;
            }
        """)
        panel_layout = QVBoxLayout(self.panel)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        
        # AI Status Title
        self.title_label = QLabel("ANTIGRAVITY AI")
        self.title_label.setFont(QFont("Outfit", 12, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: rgba(148, 163, 184, 1.0); background: transparent; border: none;")
        
        # Main Suggestion Label
        self.status_label = QLabel("ANALYZING...")
        self.status_label.setFont(QFont("Outfit", 20, QFont.Weight.Black))
        self.status_label.setStyleSheet("color: #38bdf8; background: transparent; border: none;")
        
        # Detail / Confidence Label
        self.info_label = QLabel("Waiting for game state...")
        self.info_label.setFont(QFont("Inter", 13))
        self.info_label.setStyleSheet("color: #cbd5e1; background: transparent; border: none;")
        
        panel_layout.addWidget(self.title_label)
        panel_layout.addWidget(self.status_label)
        panel_layout.addWidget(self.info_label)
        
        self.main_layout.addWidget(self.panel)

    def _animate(self):
        """Update animation tick and repaint."""
        self.anim_tick = (self.anim_tick + 1) % 360
        self.update()

    def update_status(self, text):
        """Update the main suggestion text with a color check."""
        self.status_label.setText(text.upper())
        if "PLAY" in text.upper():
            self.status_label.setStyleSheet("color: #4ade80; background: transparent; border: none;") # Green
        elif "ATTACK" in text.upper():
            self.status_label.setStyleSheet("color: #f87171; background: transparent; border: none;") # Red
        else:
            self.status_label.setStyleSheet("color: #38bdf8; background: transparent; border: none;") # Blue

    def update_info(self, text):
        self.info_label.setText(text)
        
    def set_arrow(self, start, end):
        self.arrow_start = start
        self.arrow_end = end
        self.highlight_pos = None
        self.update()
    
    def set_highlight(self, pos):
        self.highlight_pos = pos
        self.arrow_start = None
        self.arrow_end = None
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Pulse factor (0.0 to 1.0)
        pulse = (math.sin(self.anim_tick * 0.1) + 1) / 2
        
        if self.arrow_start and self.arrow_end:
            start_pt = QPointF(float(self.arrow_start.x), float(self.arrow_start.y))
            end_pt = QPointF(float(self.arrow_end.x), float(self.arrow_end.y))
            
            # --- DRAW GLOWING LINE ---
            # Outer glow
            glow_pen = QPen(QColor(56, 189, 248, 50 + int(30 * pulse)), 12)
            glow_pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            painter.setPen(glow_pen)
            painter.drawLine(start_pt, end_pt)
            
            # Main line
            line_pen = QPen(QColor(56, 189, 248, 220), 5)
            line_pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            painter.setPen(line_pen)
            painter.drawLine(start_pt, end_pt)
            
            # --- DRAW TARGET CIRCLE ---
            radius = 25 + (5 * pulse)
            grad = QRadialGradient(end_pt, radius)
            grad.setColorAt(0, QColor(56, 189, 248, 150))
            grad.setColorAt(1, QColor(56, 189, 248, 0))
            painter.setBrush(QBrush(grad))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(end_pt, radius, radius)
            
            # White core
            painter.setBrush(QColor(255, 255, 255, 200))
            painter.drawEllipse(end_pt, 4, 4)
        
        elif self.highlight_pos:
            pos = QPointF(float(self.highlight_pos.x), float(self.highlight_pos.y))
            
            # --- DRAW RADIATING RING ---
            radius = 40 + (10 * pulse)
            
            # Outer ring
            ring_pen = QPen(QColor(74, 222, 128, 200), 3)
            painter.setPen(ring_pen)
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawEllipse(pos, radius, radius)
            
            # Inner fill
            fill_grad = QRadialGradient(pos, radius)
            fill_grad.setColorAt(0, QColor(74, 222, 128, 60))
            fill_grad.setColorAt(1, QColor(74, 222, 128, 0))
            painter.setBrush(QBrush(fill_grad))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(pos, radius, radius)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OverlayWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OverlayWindow()
    window.show()
    print("Overlay started.")
    sys.exit(app.exec())
