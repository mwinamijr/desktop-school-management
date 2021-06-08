# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class HayatulApp(object):
    def __init__(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(widget)
        self.loginButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.logo = QtWidgets.QLabel(widget)
        self.loginTitle = QtWidgets.QLabel(widget)

    def login_ui(self, login):
        login.setObjectName("widget")
        login.resize(1000, 804)
        login.setMinimumSize(QtCore.QSize(1000, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        login.setLayoutDirection(QtCore.Qt.LeftToRight)
        login.setStyleSheet("background-color:#293b5f;")

        # Logo
        self.logo.setGeometry(QtCore.QRect(200, 40, 600, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.logo.setFont(font)
        self.logo.setStyleSheet("color: #dbe6fd;\n"
                                "font-size: 100px;\n"
                                "font-family: Castellar"
                                )
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")

        # Login title
        self.loginTitle.setGeometry(QtCore.QRect(0, 190, 1000, 121))
        self.loginTitle.setStyleSheet("color: #dbe6fd;\n"
                                      "width: 100%;\n"
                                      "font-size: 40pt"
                                      )
        self.loginTitle.setTextFormat(QtCore.Qt.PlainText)
        self.loginTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.loginTitle.setObjectName("loginTitle")

        # Login form layout
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 340, 691, 442))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Username
        self.username.setStyleSheet("margin-left:40px;\n"
                                    "margin-right:40px;\n"
                                    "color: grey;\n"
                                    "border: 1px solid grey;\n"
                                    "border-radius:20px;\n"
                                    "border-bottom:3px solid white;\n"
                                    "padding: 5px;\n"
                                    "padding-left: 15px;\n"
                                    "font-size: 30pt"
                                    )
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)

        # Password
        self.password.setStyleSheet("margin-left:40px;\n"
                                    "margin-right:40px;\n"
                                    "color: grey;\n"
                                    "border: 1px solid grey;\n"
                                    "border-radius:20px;\n"
                                    "border-bottom:3px solid white;\n"
                                    "padding: 5px;\n"
                                    "padding-left: 15px;\n"
                                    "font-size: 30pt"
                                    )
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.password)

        # Login button
        self.loginButton.setStyleSheet("border: 4px solid \'#2541b2\';\n"
                                       " border-radius: 45px;\n"
                                       "font-size: 35px;\n"
                                       "color: \'white\';\n"
                                       "padding: 25px 0;\n"
                                       " margin: 10px 200px;")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("widget", "Hayatul Islamiya SIS"))
        self.loginTitle.setText(_translate("widget", "Log in"))
        self.logo.setText(_translate("widget", "Hayatul"))
        self.username.setPlaceholderText(_translate("widget", "Username"))
        self.password.setPlaceholderText(_translate("widget", "Password"))
        self.loginButton.setText(_translate("widget", "login"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = HayatulApp()
    ui.login_ui(widget)
    widget.show()
    sys.exit(app.exec_())
