import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QPainter, QBrush, QFont
from PyQt5.QtCore import QPropertyAnimation, QPoint, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowIcon(QIcon("Assets\chatgpt-logo-02AFA704B5-seeklogo.com.png"))
        self.setWindowTitle("My Desktop Application")
        self.resize(400, 200)
        
        self.label_username = QLabel("Username", self)
        self.label_username.move(50, 50)
        
        self.text_username = QLineEdit(self)
        self.text_username.move(150, 50)
        
        self.label_password = QLabel("Password", self)
        self.label_password.move(50, 80)
        
        self.text_password = QLineEdit(self)
        self.text_password.move(150, 80)
        self.text_password.setEchoMode(QLineEdit.Password)
        
        self.button_login = QPushButton("Login", self)
        self.button_login.move(150, 120)
        self.button_login.clicked.connect(self.login)

        self.animation = QPropertyAnimation(self.label_username, b"pos")
        self.animation.setDuration(1000)
        self.animation.setStartValue(QPoint(100,50))
        self.animation.setEndValue(QPoint(400,50))

        font = QFont("Verdana", 10)
        self.label_username.setFont(font)
        self.label_password.setFont(font)

    def paintEvent(self, event):
        painter = QPainter(self)
        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(Qt.gray)
        painter.fillRect(event.rect(), brush)
        

    def login(self):
        username = self.text_username.text()
        password = self.text_password.text()
        
        response = requests.post('http://example.com/api/login/', data={'username': username, 'password': password})
        
        if response.status_code == 200:
            self.label_message = QLabel("Logged in successfully!", self)
            self.label_message.move(50, 160)
        else:
            self.label_message = QLabel("Incorrect username or password.", self)
            self.label_message.move(50, 160)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
