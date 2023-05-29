import os
import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920, 1080)
        self.setWindowTitle("Website Designer")
        self.x = 0
        self.y = 0

        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: yellow")
        self.label.setFixedSize(50, 50) # You can adjust the size of the highlight
        self.label.hide()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.label.hide)

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        self.generate_code()

        self.label.move(self.x, self.y)
        self.label.show()
        self.timer.start(3000) # The highlight will be shown for 3 seconds

    def generate_code(self):
        now = datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d_%H-%M-%S")

        php_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <link rel="stylesheet" type="text/css" href="style_{timestamp_str}.css">
        </head>
        <body>
        <div class="text">Here</div>
        </body>
        </html>
        """

        css_code = f"""
        .text {{
            position: absolute;
            left: {self.x}px;
            top: {self.y}px;
        }}
        """
        
        if not os.path.exists('output'):
            os.makedirs('output')

        with open(f"output/output_{timestamp_str}.php", "w") as f:
            f.write(php_code)

        with open(f"output/style_{timestamp_str}.css", "w") as f:
            f.write(css_code)

        print(f"PHP and CSS code generated with text at ({self.x}, {self.y}). Open output/output_{timestamp_str}.php and output/style_{timestamp_str}.css to view it.")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())
