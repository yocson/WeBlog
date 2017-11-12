# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSettings
import BH
import ac

class Ui_BLOGHELPER(object):
    def setupUi(self, BLOGHELPER):
        BLOGHELPER.setObjectName("BLOGHELPER")
        BLOGHELPER.resize(430, 772)
        self.centralwidget = QtWidgets.QWidget(BLOGHELPER)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filesrc = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("pingfang")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.filesrc.setFont(font)
        self.filesrc.setStyleSheet("font: 15pt \"pingfang\";")
        self.filesrc.setObjectName("filesrc")
        self.horizontalLayout_2.addWidget(self.filesrc)
        self.src = QtWidgets.QLineEdit(self.centralwidget)
        self.src.setText("")
        self.src.setFrame(False)
        self.src.setObjectName("src")
        self.horizontalLayout_2.addWidget(self.src)
        self.choosefile = QtWidgets.QToolButton(self.centralwidget)
        self.choosefile.setObjectName("choosefile")
        self.horizontalLayout_2.addWidget(self.choosefile)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filedes = QtWidgets.QLabel(self.centralwidget)
        self.filedes.setStyleSheet("font: 15pt \"pingfang\";")
        self.filedes.setObjectName("filedes")
        self.horizontalLayout_3.addWidget(self.filedes)
        self.des = QtWidgets.QLineEdit(self.centralwidget)
        self.des.setText("")
        self.des.setFrame(False)
        self.des.setObjectName("des")
        self.horizontalLayout_3.addWidget(self.des)
        self.choosedes = QtWidgets.QToolButton(self.centralwidget)
        self.choosedes.setObjectName("choosedes")
        self.horizontalLayout_3.addWidget(self.choosedes)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.filetitle = QtWidgets.QLabel(self.centralwidget)
        self.filetitle.setStyleSheet("font: 15pt \"pingfang\";")
        self.filetitle.setObjectName("filetitle")
        self.verticalLayout.addWidget(self.filetitle)
        self.categories = QtWidgets.QLabel(self.centralwidget)
        self.categories.setStyleSheet("font: 15pt \"pingfang\";")
        self.categories.setObjectName("categories")
        self.verticalLayout.addWidget(self.categories)
        self.tag1 = QtWidgets.QLabel(self.centralwidget)
        self.tag1.setStyleSheet("font: 15pt \"pingfang\";")
        self.tag1.setObjectName("tag1")
        self.verticalLayout.addWidget(self.tag1)
        self.tag2 = QtWidgets.QLabel(self.centralwidget)
        self.tag2.setStyleSheet("font: 15pt \"pingfang\";")
        self.tag2.setObjectName("tag2")
        self.verticalLayout.addWidget(self.tag2)
        self.tag3 = QtWidgets.QLabel(self.centralwidget)
        self.tag3.setStyleSheet("font: 15pt \"pingfang\";")
        self.tag3.setObjectName("tag3")
        self.verticalLayout.addWidget(self.tag3)
        self.author = QtWidgets.QLabel(self.centralwidget)
        self.author.setStyleSheet("font: 15pt \"pingfang\";")
        self.author.setObjectName("author")
        self.verticalLayout.addWidget(self.author)
        self.filename = QtWidgets.QLabel(self.centralwidget)
        self.filename.setStyleSheet("font: 15pt \"pingfang\";")
        self.filename.setObjectName("filename")
        self.verticalLayout.addWidget(self.filename)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filetitle_text = QtWidgets.QLineEdit(self.centralwidget)
        self.filetitle_text.setFrame(False)
        self.filetitle_text.setObjectName("filetitle_text")
        self.verticalLayout_2.addWidget(self.filetitle_text)
        self.categories_text = QtWidgets.QLineEdit(self.centralwidget)
        self.categories_text.setFrame(False)
        self.categories_text.setObjectName("categories_text")
        self.verticalLayout_2.addWidget(self.categories_text)
        self.tag1_text = QtWidgets.QLineEdit(self.centralwidget)
        self.tag1_text.setFrame(False)
        self.tag1_text.setObjectName("tag1_text")
        self.verticalLayout_2.addWidget(self.tag1_text)
        self.tag2_text = QtWidgets.QLineEdit(self.centralwidget)
        self.tag2_text.setFrame(False)
        self.tag2_text.setObjectName("tag2_text")
        self.verticalLayout_2.addWidget(self.tag2_text)
        self.tag3_text = QtWidgets.QLineEdit(self.centralwidget)
        self.tag3_text.setFrame(False)
        self.tag3_text.setObjectName("tag3_text")
        self.verticalLayout_2.addWidget(self.tag3_text)
        self.author_text = QtWidgets.QLineEdit(self.centralwidget)
        self.author_text.setFrame(False)
        self.author_text.setObjectName("author_text")
        self.verticalLayout_2.addWidget(self.author_text)
        self.filename_text = QtWidgets.QLineEdit(self.centralwidget)
        self.filename_text.setFrame(False)
        self.filename_text.setObjectName("filename_text")
        self.verticalLayout_2.addWidget(self.filename_text)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 13, 0, 1, 2)
        self.addfm = QtWidgets.QCheckBox(self.centralwidget)
        self.addfm.setStyleSheet("font: 20pt \"pingfang\";")
        self.addfm.setObjectName("addfm")
        self.gridLayout.addWidget(self.addfm, 8, 0, 1, 1)
        self.uploadimg = QtWidgets.QCheckBox(self.centralwidget)
        self.uploadimg.setStyleSheet("font: 20pt \"pingfang\";")
        self.uploadimg.setObjectName("uploadimg")
        self.gridLayout.addWidget(self.uploadimg, 16, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setStyleSheet("font: 15pt \"pingfang\";")
        self.quit.setObjectName("quit")
        self.horizontalLayout_4.addWidget(self.quit)
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setStyleSheet("font: 15pt \"pingfang\";")
        self.run.setObjectName("run")
        self.horizontalLayout_4.addWidget(self.run)
        self.gridLayout.addLayout(self.horizontalLayout_4, 21, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 18, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 16pt \"pingfang\";\n"
"color:rgb(102, 102, 102)")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 17, 0, 1, 1)
        self.Title = QtWidgets.QLabel(self.centralwidget)
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
        self.gridLayout.addWidget(self.Title, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 14, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 16pt \"pingfang\";\n"
"color:rgb(102, 102, 102)")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font: 16pt \"pingfang\";\n"
"color:rgb(102, 102, 102)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 16pt \"pingfang\";\n"
"color:rgb(102, 102, 102)")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 22, 0, 1, 2)
        BLOGHELPER.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BLOGHELPER)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 22))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        BLOGHELPER.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BLOGHELPER)
        self.statusbar.setObjectName("statusbar")
        BLOGHELPER.setStatusBar(self.statusbar)
        self.actionAccounts = QtWidgets.QAction(BLOGHELPER)
        self.actionAccounts.setObjectName("actionAccounts")
        self.menuSettings.addAction(self.actionAccounts)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(BLOGHELPER)
        self.quit.clicked.connect(BLOGHELPER.close)
        QtCore.QMetaObject.connectSlotsByName(BLOGHELPER)

        self.connection()

    def retranslateUi(self, BLOGHELPER):
        _translate = QtCore.QCoreApplication.translate
        BLOGHELPER.setWindowTitle(_translate("BLOGHELPER", "WeBlog"))
        self.filesrc.setText(_translate("BLOGHELPER", "Source File"))
        self.choosefile.setText(_translate("BLOGHELPER", "..."))
        self.filedes.setText(_translate("BLOGHELPER", "File Desination"))
        self.choosedes.setText(_translate("BLOGHELPER", "..."))
        self.filetitle.setText(_translate("BLOGHELPER", "Title"))
        self.categories.setText(_translate("BLOGHELPER", "Categories"))
        self.tag1.setText(_translate("BLOGHELPER", "Tag 1"))
        self.tag2.setText(_translate("BLOGHELPER", "Tag 2"))
        self.tag3.setText(_translate("BLOGHELPER", "Tag 3"))
        self.author.setText(_translate("BLOGHELPER", "Author"))
        self.filename.setText(_translate("BLOGHELPER", "Filename"))
        self.addfm.setText(_translate("BLOGHELPER", "Add Front Matter(YAML)"))
        self.uploadimg.setText(_translate("BLOGHELPER", "Upload Images"))
        self.quit.setText(_translate("BLOGHELPER", "Quit!"))
        self.run.setText(_translate("BLOGHELPER", "Run"))
        self.label_4.setText(_translate("BLOGHELPER", "Make sure you have already set your account"))
        self.Title.setText(_translate("BLOGHELPER", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">WeBlog</span></p></body></html>"))
        self.label_3.setText(_translate("BLOGHELPER", "Choose file and file destination:"))
        self.label_2.setText(_translate("BLOGHELPER", "Enter your front matter information:"))
        self.menuSettings.setTitle(_translate("BLOGHELPER", "Settings"))
        self.actionAccounts.setText(_translate("BLOGHELPER", "Accounts"))
        

    def connection(self):
        self.file_name = ''
        self.des_dirname = ''
        self.readInfo()
        self.choosefile.clicked.connect(self.get_file)
        self.run.clicked.connect(self.helper)
        self.choosedes.clicked.connect(self.to_file)

        self.actionAccounts.triggered.connect(self.set_account)

    def set_account(self):
        self.Account = QtWidgets.QWidget()
        self.acset = ac.Ui_Account()
        self.acset.setupUi(self.Account)
        self.acset.Save.clicked.connect(self.saveInfo)
        self.acset.readSavedInfo(self.key_list)
        self.Account.show()
        

    def saveInfo(self):
        self.settings = QSettings("Yocson", "WeBlog")
        self.key_list[0] = self.acset.ACCESS_KEY_enter.text()
        self.key_list[1] = self.acset.SECRET_KEY_enter.text()
        self.key_list[2] = self.acset.LINK_DOMAIN_enter.text()
        self.key_list[3] = self.acset.BUCKET_NAME_enter.text()
        self.settings.setValue('key_list', self.key_list)
        del self.settings
        self.Account.close()

    def readInfo(self):
        self.settings = QSettings("Yocson", "WeBlog")
        # key_list[0] = settings.value('ACCESS_KEY')
        # key_list[1] = settings.value('SECRET_KEY')
        # key_list[2] = settings.value('LINK_DOMAIN')
        # key_list[3] = settings.value('BUCKET_NAME')
        self.key_list = self.settings.value("key_list", defaultValue=["","","",""])


    def get_file(self):
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(caption='open file', directory='/',filter='*.md')[0]
        if self.file_name:
            print(self.file_name)
            self.src.setText(self.file_name)

    def to_file(self):
        self.des_dirname = QtWidgets.QFileDialog.getExistingDirectory(caption='choose destination directory ', directory='/')
        if self.des_dirname:
            print(self.des_dirname)
            self.des.setText(self.des_dirname)

    def helper(self):
        if self.file_name:
            para_list = {'title': self.filetitle_text.text(),
                         'categories': self.categories_text.text(),
                         'tags': [self.tag1_text.text(), self.tag2_text.text(),self.tag3_text.text()],
                         'author': self.author_text.text()
                         }
            new_filename = self.filename_text.text()
            bH = BH.BlogHelper(self.file_name, self.des_dirname, para_list, new_filename, self.key_list)
            original_text = bH.readfile()
            
            #add yaml and upload images
            if self.addfm.isChecked() and self.uploadimg.isChecked():
                yaml_text = bH.addyaml()
                text_after_up = bH.uploadimages(original_text)
                bH.writefile(yaml_text, text_after_up, False)
                self.textBrowser.setText(yaml_text)
            #add yaml alone
            elif self.addfm.isChecked():
                yaml_text = bH.addyaml()
                bH.writefile(yaml_text, original_text, False)
                self.textBrowser.setText(yaml_text)
            #upload alone
            else:
                yaml_text = ""
                text_after_up = bH.uploadimages(original_text)
                bH.writefile(yaml_text, text_after_up, True)
                self.textBrowser.setText("Images uploaded Successfully!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BLOGHELPER = QtWidgets.QMainWindow()
    ui = Ui_BLOGHELPER()
    ui.setupUi(BLOGHELPER)
    BLOGHELPER.show()
    sys.exit(app.exec_())

