# Form implementation generated from reading ui file 'Anasayfa.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 750)
        MainWindow.setStyleSheet(".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: red;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 841, 371))
        self.groupBox.setObjectName("groupBox")
        self.lwBrans = QtWidgets.QListWidget(self.groupBox)
        self.lwBrans.setGeometry(QtCore.QRect(40, 290, 256, 81))
        self.lwBrans.setObjectName("lwBrans")
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lwBrans.addItem(item)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 270, 61, 16))
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 259, 233))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lneTCK = QtWidgets.QLineEdit(self.layoutWidget)
        self.lneTCK.setMaxLength(11)
        self.lneTCK.setObjectName("lneTCK")
        self.horizontalLayout.addWidget(self.lneTCK)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lneSporcuAdi = QtWidgets.QLineEdit(self.layoutWidget)
        self.lneSporcuAdi.setObjectName("lneSporcuAdi")
        self.horizontalLayout_2.addWidget(self.lneSporcuAdi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lneSpocuSoyadi = QtWidgets.QLineEdit(self.layoutWidget)
        self.lneSpocuSoyadi.setObjectName("lneSpocuSoyadi")
        self.horizontalLayout_3.addWidget(self.lneSpocuSoyadi)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.cmbSporKlubu = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbSporKlubu.setObjectName("cmbSporKlubu")
        self.cmbSporKlubu.addItem("")
        self.cmbSporKlubu.addItem("")
        self.cmbSporKlubu.addItem("")
        self.cmbSporKlubu.addItem("")
        self.cmbSporKlubu.addItem("")
        self.cmbSporKlubu.addItem("")
        self.horizontalLayout_4.addWidget(self.cmbSporKlubu)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spnKilo = QtWidgets.QSpinBox(self.layoutWidget)
        self.spnKilo.setMinimum(80)
        self.spnKilo.setMaximum(130)
        self.spnKilo.setProperty("value", 80)
        self.spnKilo.setObjectName("spnKilo")
        self.horizontalLayout_5.addWidget(self.spnKilo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.cmbCinsiyet = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbCinsiyet.setObjectName("cmbCinsiyet")
        self.cmbCinsiyet.addItem("")
        self.cmbCinsiyet.addItem("")
        self.horizontalLayout_6.addWidget(self.cmbCinsiyet)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.chkMedeniHal = QtWidgets.QCheckBox(self.layoutWidget)
        self.chkMedeniHal.setObjectName("chkMedeniHal")
        self.horizontalLayout_7.addWidget(self.chkMedeniHal)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.cwDtarihi = QtWidgets.QCalendarWidget(self.groupBox)
        self.cwDtarihi.setGeometry(QtCore.QRect(380, 70, 301, 201))
        self.cwDtarihi.setObjectName("cwDtarihi")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(370, 30, 101, 16))
        self.label_8.setObjectName("label_8")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(880, 30, 102, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnEkle = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnEkle.setObjectName("btnEkle")
        self.verticalLayout_2.addWidget(self.btnEkle)
        self.btnSil = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnSil.setObjectName("btnSil")
        self.verticalLayout_2.addWidget(self.btnSil)
        self.btnAra = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnAra.setObjectName("btnAra")
        self.verticalLayout_2.addWidget(self.btnAra)
        self.btnGncelle = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnGncelle.setObjectName("btnGncelle")
        self.verticalLayout_2.addWidget(self.btnGncelle)
        self.btnListele = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnListele.setObjectName("btnListele")
        self.verticalLayout_2.addWidget(self.btnListele)
        self.btnCikis = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnCikis.setObjectName("btnCikis")
        self.verticalLayout_2.addWidget(self.btnCikis)
        self.tblwSporcuBilgi = QtWidgets.QTableWidget(self.centralwidget)
        self.tblwSporcuBilgi.setGeometry(QtCore.QRect(30, 390, 911, 251))
        self.tblwSporcuBilgi.setRowCount(14)
        self.tblwSporcuBilgi.setColumnCount(10)
        self.tblwSporcuBilgi.setObjectName("tblwSporcuBilgi")
        self.lblKayitSayisi = QtWidgets.QLabel(self.centralwidget)
        self.lblKayitSayisi.setGeometry(QtCore.QRect(50, 656, 81, 20))
        self.lblKayitSayisi.setObjectName("lblKayitSayisi")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(140, 660, 60, 16))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 36))
        self.menubar.setObjectName("menubar")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.menu_Hakkimda = QtGui.QAction(MainWindow)
        self.menu_Hakkimda.setObjectName("menu_Hakkimda")
        self.actionUla = QtGui.QAction(MainWindow)
        self.actionUla.setObjectName("actionUla")
        self.menuYard_m.addAction(self.menu_Hakkimda)
        self.menuYard_m.addAction(self.actionUla)
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        self.cmbSporKlubu.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Sporcu Bilgileri"))
        __sortingEnabled = self.lwBrans.isSortingEnabled()
        self.lwBrans.setSortingEnabled(False)
        item = self.lwBrans.item(0)
        item.setText(_translate("MainWindow", "Güreş"))
        item = self.lwBrans.item(1)
        item.setText(_translate("MainWindow", "Basketbol"))
        item = self.lwBrans.item(2)
        item.setText(_translate("MainWindow", "Futbol"))
        item = self.lwBrans.item(3)
        item.setText(_translate("MainWindow", "Badminton"))
        item = self.lwBrans.item(4)
        item.setText(_translate("MainWindow", "Boks"))
        self.lwBrans.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(_translate("MainWindow", "Branşı  :"))
        self.label.setText(_translate("MainWindow", "TC kimlik numarası :"))
        self.label_2.setText(_translate("MainWindow", "Sporcu Adı:"))
        self.label_3.setText(_translate("MainWindow", "Sporcu Soyadı :"))
        self.label_4.setText(_translate("MainWindow", "Spor Klübü :"))
        self.cmbSporKlubu.setItemText(0, _translate("MainWindow", "KSK"))
        self.cmbSporKlubu.setItemText(1, _translate("MainWindow", "BJK"))
        self.cmbSporKlubu.setItemText(2, _translate("MainWindow", "FB"))
        self.cmbSporKlubu.setItemText(3, _translate("MainWindow", "GS"))
        self.cmbSporKlubu.setItemText(4, _translate("MainWindow", "EFES"))
        self.cmbSporKlubu.setItemText(5, _translate("MainWindow", "BANVİT"))
        self.label_5.setText(_translate("MainWindow", "Sporcu Kilosu :"))
        self.label_6.setText(_translate("MainWindow", "Sporcu Cinsiyeti :"))
        self.cmbCinsiyet.setItemText(0, _translate("MainWindow", "Erkek"))
        self.cmbCinsiyet.setItemText(1, _translate("MainWindow", "Kadın"))
        self.label_7.setText(_translate("MainWindow", "Medeni Hali:"))
        self.chkMedeniHal.setText(_translate("MainWindow", "Evli"))
        self.label_8.setText(_translate("MainWindow", "Doğum Tarihi :"))
        self.btnEkle.setText(_translate("MainWindow", "Kayıt Ekle"))
        self.btnSil.setText(_translate("MainWindow", "Kayıt Sil"))
        self.btnAra.setText(_translate("MainWindow", "Kayıt Ara"))
        self.btnGncelle.setText(_translate("MainWindow", "Güncelle"))
        self.btnListele.setText(_translate("MainWindow", "Listele"))
        self.btnCikis.setText(_translate("MainWindow", "Çıkış"))
        self.lblKayitSayisi.setText(_translate("MainWindow", "KayıtSayısı :"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menu_Hakkimda.setText(_translate("MainWindow", "Hakkımda"))
        self.actionUla.setText(_translate("MainWindow", "Ulaş"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
