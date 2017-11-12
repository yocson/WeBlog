# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Account(object):
    def setupUi(self, Account):
        Account.setObjectName("Account")
        Account.resize(435, 255)
        self.gridLayout = QtWidgets.QGridLayout(Account)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel = QtWidgets.QPushButton(Account)
        self.cancel.setStyleSheet("font: 15pt \"pingfang\";")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.Save = QtWidgets.QPushButton(Account)
        self.Save.setStyleSheet("font: 15pt \"pingfang\";")
        self.Save.setObjectName("Save")
        self.horizontalLayout.addWidget(self.Save)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ACCESS_KEY = QtWidgets.QLabel(Account)
        self.ACCESS_KEY.setStyleSheet("font: 15pt \"pingfang\";")
        self.ACCESS_KEY.setObjectName("ACCESS_KEY")
        self.gridLayout_2.addWidget(self.ACCESS_KEY, 0, 0, 1, 1)
        self.ACCESS_KEY_enter = QtWidgets.QLineEdit(Account)
        self.ACCESS_KEY_enter.setText("")
        self.ACCESS_KEY_enter.setObjectName("ACCESS_KEY_enter")
        self.gridLayout_2.addWidget(self.ACCESS_KEY_enter, 0, 1, 1, 1)
        self.SECRET_KEY = QtWidgets.QLabel(Account)
        self.SECRET_KEY.setStyleSheet("font: 15pt \"pingfang\";")
        self.SECRET_KEY.setObjectName("SECRET_KEY")
        self.gridLayout_2.addWidget(self.SECRET_KEY, 1, 0, 1, 1)
        self.SECRET_KEY_enter = QtWidgets.QLineEdit(Account)
        self.SECRET_KEY_enter.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SECRET_KEY_enter.setObjectName("SECRET_KEY_enter")
        self.gridLayout_2.addWidget(self.SECRET_KEY_enter, 1, 1, 1, 1)
        self.LINK_DOMAIN = QtWidgets.QLabel(Account)
        self.LINK_DOMAIN.setStyleSheet("font: 15pt \"pingfang\";")
        self.LINK_DOMAIN.setObjectName("LINK_DOMAIN")
        self.gridLayout_2.addWidget(self.LINK_DOMAIN, 2, 0, 1, 1)
        self.LINK_DOMAIN_enter = QtWidgets.QLineEdit(Account)
        self.LINK_DOMAIN_enter.setObjectName("LINK_DOMAIN_enter")
        self.gridLayout_2.addWidget(self.LINK_DOMAIN_enter, 2, 1, 1, 1)
        self.BUCKET_NAME = QtWidgets.QLabel(Account)
        self.BUCKET_NAME.setStyleSheet("font: 15pt \"pingfang\";")
        self.BUCKET_NAME.setObjectName("BUCKET_NAME")
        self.gridLayout_2.addWidget(self.BUCKET_NAME, 3, 0, 1, 1)
        self.BUCKET_NAME_enter = QtWidgets.QLineEdit(Account)
        self.BUCKET_NAME_enter.setObjectName("BUCKET_NAME_enter")
        self.gridLayout_2.addWidget(self.BUCKET_NAME_enter, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 1)
        self.Title = QtWidgets.QLabel(Account)
        self.Title.setMinimumSize(QtCore.QSize(0, 51))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setStyleSheet("font: 72pt;")
        self.Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 0, 0, 1, 1)

        self.retranslateUi(Account)
        self.cancel.clicked.connect(Account.close)
        QtCore.QMetaObject.connectSlotsByName(Account)


    def retranslateUi(self, Account):
        _translate = QtCore.QCoreApplication.translate
        Account.setWindowTitle(_translate("Account", "Account"))
        self.cancel.setText(_translate("Account", "Cancel"))
        self.Save.setText(_translate("Account", "Save"))
        self.ACCESS_KEY.setText(_translate("Account", "ACCESS_KEY"))
        self.SECRET_KEY.setText(_translate("Account", "SECRET_KEY"))
        self.LINK_DOMAIN.setText(_translate("Account", "LINK_DOMAIN"))
        self.BUCKET_NAME.setText(_translate("Account", "BUCKET_NAME"))
        self.Title.setText(_translate("Account", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Account Setting</span></p></body></html>"))

    def readSavedInfo(self, key_list):
        self.ACCESS_KEY_enter.setText(key_list[0])
        self.SECRET_KEY_enter.setText(key_list[1])
        self.LINK_DOMAIN_enter.setText(key_list[2])
        self.BUCKET_NAME_enter.setText(key_list[3])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account = QtWidgets.QWidget()
    ui = Ui_Account()
    ui.setupUi(Account)
    Account.show()
    sys.exit(app.exec_())

