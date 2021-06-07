import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFormLayout, QGridLayout
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Hayatul Islamiya SIS")
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

image = QPixmap('logo.png')


window.show()
sys.exit(app.exec_())