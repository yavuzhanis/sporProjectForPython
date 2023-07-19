#! -------------------------- KÜTÜPHANELER :
import sqlite3
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from AnasayfaUI import *
#!-------------------------------

# ? uygulama Oluşturma Alanı :

Uygulama = QApplication(sys.argv)  # ! Uygulama oluşturma Komutu
penAna = QMainWindow()  # Pencere OluşturmaAlanı
ui = Ui_MainWindow()
ui.setupUi(penAna)  # ! Oluşturulan pencereyi Tasarım ile birleştir

penAna.show()  # ! Pencereyi gösterme


#!----------------------VERİTABANI-----------------------------#
global curs
global conn

conn = sqlite3.connect('veritabani.db')
curs = conn.cursor()
sorguCreTblSpor = ("CREATE TABLE IF NOT EXISTS spor(                 \
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,    \
                 TCNo TEXT NOT NULL UNIQUE,                        \
                 SporcuAdi TEXT NOT NULL,                          \
                 SporcuSoyadi TEXT NOT NULL,                       \
                 KulupAdi TEXT NOT NULL,                           \
                 Brans TEXT NOT NULL,                              \
                 Cinsiyet TEXT NOT NULL,                           \
                 DTarihi TEXT NOT NULL,                            \
                 MHal TEXT NOT NULL,                               \
                 Kilo TEXT NOT NULL)")
curs.execute(sorguCreTblSpor)
conn.commit()
#?---------------------------------------------------------#


#!----------------------EKLE-----------------------------#

def EKLE():
    _lneTCK = ui.lneTCK.text()
    _lneSporcuAdi = ui.lneSporcuAdi.text()
    _lneSporcuSoyadi = ui.lneSpocuSoyadi.text()
    _cmbSporKulubu = ui.cmbSporKlubu.currentText()
    _lwBrans = ui.lwBrans.currentItem().text()
    _cmbCinsiyet = ui.cmbCinsiyet.currentText()
    _cwDtarihi = ui.cwDtarihi.selectedDate().toString()
    #! MedeniHal Fonks:
    if ui.chkMedeniHal.isChecked():
        _medeniHal = 'Evli'
    else:
        _medeniHal = 'Bekar'
    _spnKilo = ui.spnKilo.value()

    #! SORGU:
    curs.execute("INSERT INTO spor \
                     (TCNo,SporcuAdi,SporcuSoyadi,KulupAdi,Brans,Cinsiyet,Dtarihi,MHal,Kilo) \
                      VALUES (?,?,?,?,?,?,?,?,?)",
                 (_lneTCK, _lneSporcuAdi, _lneSporcuSoyadi, _cmbSporKulubu, _lwBrans, _cmbCinsiyet,
                  _cwDtarihi, _medeniHal, _spnKilo))
    conn.commit()

    LISTELE()

#?---------------------------------------------------------#


#!----------------------LİSTELE-----------------------------#
def LISTELE():
    ui.tblwSporcuBilgi.clear()
    #! setHorizontalHeaderLabels sütünları belirtmek
    ui.tblwSporcuBilgi.setHorizontalHeaderLabels(('No', 'TC Kimlik No', 'Sporcu Adı', 'Sporcu Soyadı',
                                                  'Kulüp Adı', 'Branş', 'Cinsiyet', 'Doğum Tarihi',
                                                  'Medeni Hal', 'Sporcu Kilosu'))

    ui.tblwSporcuBilgi.horizontalHeader().setSectionResizeMode(
        QHeaderView.ResizeMode.Stretch)

    curs.execute("SELECT * FROM spor")

    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwSporcuBilgi.setItem(
                satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

    ui.lneTCK.clear()
    ui.lneSpocuSoyadi.clear()
    ui.lneSporcuAdi.clear()
    ui.cmbSporKlubu.setCurrentIndex(-1)
    ui.spnKilo.setValue(55)

    curs.execute("SELECT COUNT(*) FROM spor ")
    kayıtSayisi = curs.fetchone()  # ! Tek Değer getirme
    ui.lblKayitSayisi.setText(str(kayıtSayisi[0]))


LISTELE()

#---------------------------------------------------#
#?----------------------ÇIKIŞ-----------------------------#


def CIKIS():
    cevap = QMessageBox.question(penAna, "ÇIKIŞ", "Programdan çıkmak istediğinize emin misiniz?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    if cevap == QMessageBox.StandardButton.Yes:
        conn.close()
        sys.exit(Uygulama.exec())
    else:
        penAna.show()
#!---------------------------------------------------------#


#!----------------------SİL-----------------------------#
def SIL():
    cevap = QMessageBox.question(penAna, "KAYIT SİL", "Kaydı silmek istediğinize emin misiniz?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    if cevap == QMessageBox.StandardButton.Yes:
        secili = ui.tblwSporcuBilgi.selectedItems()
        silinecek = secili[0].text()
        try:
            curs.execute("DELETE FROM spor WHERE TCNo='%s'" % (silinecek))
            conn.commit()

            LISTELE()

            ui.statusbar.showMessage(
                "KAYIT SİLME İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ...", 10000)
        except Exception as Hata:
            ui.statusbar.showMessage(
                "Şöyle bir hata ile karşılaşıldı:"+str(Hata))
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi...", 10000)


#!----------------------ARA-----------------------------#
def ARA():
    aranan1 = ui.lneTCK.text()
    aranan2 = ui.lneSporcuAdi.text()
    aranan3 = ui.lneSpocuSoyadi.text()
    curs.execute("SELECT * FROM spor WHERE TCNo=? OR SporcuAdi=? OR SporcuSoyadi=? OR (SporcuAdi=? AND SporcuSoyadi=?)",
                 (aranan1, aranan2, aranan3, aranan2, aranan3))
    conn.commit()
    ui.tblwSporcuBilgi.clear()
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblwSporcuBilgi.setItem(
                satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

#?----------------------ARA-----------------------------#


#!----------------------DOLDUR-----------------------------#
def DOLDUR():
    secili = ui.tblwSporcuBilgi.selectedItems()  # ! Değişkeni Alma
    ui.lneTCK.setText(secili[1].text()) # !1.sıra
    ui.lneSporcuAdi.setText(secili[2].text())  # 2.sıra
    ui.lneSpocuSoyadi.setText(secili[3].text())  # ? 3.sıra
    ui.cmbSporKlubu.setCurrentText(secili[4].text())  # TODO 4.SIRA
    if secili[5].text() == 'Güreş':
        ui.lwBrans.setCurrentRow(0)  # TODO İLK ELEMAN
    if secili[5].text() == 'Basketbol':
        ui.lwBrans.setCurrentRow(1)  # TODO İLK ELEMAN
    if secili[5].text() == 'Futbol':
        ui.lwBrans.setCurrentRow(2)  # TODO İLK ELEMAN
    if secili[5].text() == 'Badminton':
        ui.lwBrans.setCurrentRow(3)  # TODO İLK ELEMAN
    if secili[5].text() == 'Boks':
        ui.lwBrans.setCurrentRow(4)  # TODO İLK ELEMAN
    ui.cmbCinsiyet.setCurrentText(secili[6].text())
    # ? DATE :
    gun = int(secili[7].text()[0:2])
    ay = int(secili[7].text()[3:5])
    # ! 0 'dan 4'e kadar, burada tarihi parçalamış olduk. yıl için
    yil = int(secili[7].text()[6:10])
    ui.cwDtarihi.setSelectedDate(QtCore.QDate(yil, ay, gun))
    # TODO Medeni Hal :
    if secili[8].text() == 'Evli':
        ui.chkMedeniHal.setChecked(True)
    else:
        ui.chkMedeniHal.setChecked(False)
    ui.spnKilo.setValue(int(secili[9].text()))

#----------------------GÜNCELLE-----------------------------#
#---------------------------------------------------------#


def GUNCELLE():
    cevap = QMessageBox.question(penAna, "KAYIT GÜNCELLE", "Kaydı güncellemek istediğinize emin misiniz?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    if cevap == QMessageBox.StandardButton.Yes:
        try:
            secili = ui.tblwSporcuBilgi.selectedItems()
            _Id = int(secili[0].text())
            _lneTCK = ui.lneTCK.text()
            _lneSporcuAdi = ui.lneSporcuAdi.text()
            _lneSporcuSoyadi = ui.lneSporcuSoyadi.text()
            _cmbSporKulubu = ui.cmbSporKulubu.currentText()
            _lwBrans = ui.lwBrans.currentItem().text()
            _cmbCinsiyet = ui.cmbCinsiyet.currentText()
            _cwDTarihi = ui.cwDTarihi.selectedDate().toString(QtCore.Qt.ISODate)

            if ui.chkMedeniHal.isChecked():
                _medeniHal = "Evli"
            else:
                _medeniHal = "Bekar"
            _spnKilo = ui.spnKilo.value()

            curs.execute("UPDATE spor SET TCNo=?, SporcuAdi=?, SporcuSoyadi=?, Kilo=?,   \
                         KulupAdi=?, Brans=?, Cinsiyet=?, DTarihi=?, MHal=? WHERE Id=?",
                         (_lneTCK, _lneSporcuAdi, _lneSporcuSoyadi, _spnKilo,
                          _cmbSporKulubu, _lwBrans, _cmbCinsiyet, _cwDTarihi, _medeniHal, _Id))
            conn.commit()

            LISTELE()

        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata meydana geldi"+str(Hata))
    else:
        ui.statusbar.showMessage("Güncellme iptal edildi", 10000)





#?----------------------SİNYAL-SLOT-----------------------------#
ui.btnEkle.clicked.connect(EKLE)
ui.btnListele.clicked.connect(LISTELE)
ui.btnCikis.clicked.connect(CIKIS)
ui.btnSil.clicked.connect(SIL)
ui.btnAra.clicked.connect(ARA)
ui.tblwSporcuBilgi.selectionModel().selectionChanged.connect(DOLDUR)
ui.btnGncelle.clicked.connect(GUNCELLE)

#!---------------------------------------------------------#

sys.exit(Uygulama.exec())
