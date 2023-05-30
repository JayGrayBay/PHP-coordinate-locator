import os
import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QRadioButton, QVBoxLayout, QWidget, QButtonGroup, QTextEdit, QInputDialog
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        screen = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.setWindowTitle("Website Designer")
        self.setWindowTitle("Website Designer")
        self.x = 0
        self.y = 0

        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: yellow")
        self.label.setFixedSize(50, 50) # You can adjust the size of the highlight
        self.label.hide()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.label.hide)

        # Set up radio buttons
        self.content_image = QRadioButton('Image')
        self.content_box = QRadioButton('Box')
        self.content_text = QRadioButton('Text')

        # Organize radio buttons into groups
        self.content_type_group = QButtonGroup()
        self.content_type_group.addButton(self.content_image)
        self.content_type_group.addButton(self.content_box)
        self.content_type_group.addButton(self.content_text)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.content_image)
        layout.addWidget(self.content_box)
        layout.addWidget(self.content_text)

        options_widget = QWidget()
        options_widget.setLayout(layout)

        self.setCentralWidget(options_widget)

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

        php_code = ""
        css_code = ""

        if self.content_image.isChecked():
            # Here, you would need to specify the source of the image
            php_code = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <link rel="stylesheet" type="text/css" href="style_{timestamp_str}.css">
            </head>
            <body>
            <img src="your_image_source" class="image">
            </body>
            </html>
            """

            css_code = f"""
            .image {{
                position: absolute;
                left: {self.x}px;
                top: {self.y}px;
            }}
            """
        elif self.content_box.isChecked():
            php_code = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <link rel="stylesheet" type="text/css" href="style_{timestamp_str}.css">
            </head>
            <body>
            <div class="box"></div>
            </body>
            </html>
            """

            css_code = f"""
            .box {{
                position: absolute;
                left: {self.x}px;
                top: {self.y}px;
                width: 100px;  # You can adjust the size of the box
                height: 100px; # You can adjust the size of the box
                background-color: #000;  # You can adjust the color of the box
            }}
            """
        else:  # If 'Text' is selected
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

        print(f"PHP and CSS code generated. Open output/output_{timestamp_str}.php and output/style_{timestamp_str}.css to view it.")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())
