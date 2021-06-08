import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFormLayout, QGridLayout, QDialog
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore


class HayatulApplication(object):
    def setupUi(self, window):


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Hayatul Islamiya SIS")
window.setFixedWidth(1000)
window.setStyleSheet("background: #293b5f;")

grid = QGridLayout()

# display logo
# image = QPixmap('logo.png')
# logo = QLabel().setPixmap(image)
logo = QLabel("Hayatul")
logo.setAlignment(QtCore.Qt.AlignCenter)
logo.setStyleSheet(
    "margin-top: 20px;" +
    "font-size: 100px;" +
    "font-family: Monospace;" +
    "color: #dbe6fd;"
)
# login title
loginTitle = QLabel("Login")
loginTitle.setAlignment(QtCore.Qt.AlignCenter)
loginTitle.setStyleSheet(
    "margin-top: 10px;" +
    "font-size: 30px;" +
    "font-family: Monospace;" +
    "color: #dbe6fd;"
)

# login form

grid.addWidget(logo, 0, 0)
grid.addWidget(loginTitle, 1, 0)

window.setLayout(grid)
window.show()
sys.exit(app.exec_())
