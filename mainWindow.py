# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import blog_helper3
import blog_helper4
import qiniu_update
import BH

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 528)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(160, 420, 164, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 271, 51))
        self.label_2.setMinimumSize(QtCore.QSize(0, 51))
        self.label_2.setStyleSheet("font: 30pt \".SF NS Text\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 190, 241, 211))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(240, 160, 101, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(130, 160, 87, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 80, 281, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(100, 110, 281, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        self.toolButton_2 = QtWidgets.QToolButton(self.horizontalLayoutWidget_3)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_3.addWidget(self.toolButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.file_name = ''
        self.des_dirname = ''

        self.toolButton.clicked.connect(self.get_file)
        self.buttonBox.accepted.connect(self.helper)
        self.toolButton_2.clicked.connect(self.to_file)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "BlogHelper"))
        self.label_3.setText(_translate("MainWindow", "title"))
        self.label_4.setText(_translate("MainWindow", "subtitle"))
        self.label_5.setText(_translate("MainWindow", "img"))
        self.label_6.setText(_translate("MainWindow", "tag1"))
        self.label_7.setText(_translate("MainWindow", "tag2"))
        self.label_8.setText(_translate("MainWindow", "author"))
        self.label_10.setText(_translate("MainWindow", "filename"))
        self.checkBox.setText(_translate("MainWindow", "Upload imgs to Qiniu"))
        self.checkBox_2.setText(_translate("MainWindow", "Add YAML"))
        self.label.setText(_translate("MainWindow", "Source File"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_9.setText(_translate("MainWindow", "Destination"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))

    def get_file(self):
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(caption='open file', directory='/',filter='*.md')[0]
        if self.file_name:
            print(self.file_name)
            self.lineEdit.setText(self.file_name)

    def to_file(self):
        self.des_dirname = QtWidgets.QFileDialog.getExistingDirectory(caption='choose destination directory ', directory='/')
        if self.des_dirname:
            print(self.des_dirname)
            self.lineEdit_8.setText(self.des_dirname)

    def helper(self):
        if self.file_name:
            para_list = {'title': self.lineEdit_2.text(),
                         'subtitle': self.lineEdit_3.text(),
                         'header-img': self.lineEdit_4.text(),
                         'tags': [self.lineEdit_5.text(), self.lineEdit_6.text()],
                         'author': self.lineEdit_7.text()
                         }
            new_filename = self.lineEdit_9.text()
            bH = BH.BlogHelper(self.file_name, self.des_dirname, para_list, new_filename)
            original_text = bH.readfile()
            
            #add yaml and upload images
            if self.checkBox.isChecked() and self.checkBox_2.isChecked():
                yaml_text = bH.addyaml()
                text_after_up = bH.uploadimages(original_text)
                bH.writefile(yaml_text, text_after_up)
            #add yaml alone
            elif self.checkBox_2.isChecked():
                yaml_text = bH.addyaml()
                bH.writefile(yaml_text, original_text)
            #upload alone
            else:
                yaml_text = ""
                text_after_up = bH.uploadimages(original_text)
                bH.writefile(yaml_text, text_after_up)

            

