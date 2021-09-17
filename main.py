# @author: Zeynep Demirtaş

from yukleme_arayuz import Ui_MainWindow as YuklemeArayuz
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog
from PyQt5 import QtWidgets
from openpyxl import load_workbook
import sys
import grafik as grf
import time

class YuklemePenceresi(QMainWindow, YuklemeArayuz):
    def __init__(self):
        super().__init__()
        self.DosyaYolu = ''
        self.basla()
    
    def basla(self):
        self.setupUi(self)
        self.pb_grafik_cizimi.setValue(0)
        self.Aktar.clicked.connect(self.AktarFonk)
        self.manPlot.clicked.connect(self.grafik_cizdir)
       
    def DosyaSec(self):
        self.dosya_iletisim = QFileDialog(self)
        self.dosya_ac = self.dosya_iletisim.getOpenFileName(self,"Dosya Ac")
        return self.dosya_ac[0]
    
    def AktarFonk(self):
        self.DosyaYolu = self.DosyaSec()
        
    def yukleniyor(self,ilerleme_degeri):
        self.pb_grafik_cizimi.setValue(ilerleme_degeri)
        
    def grafik_cizdir(self):
        self.uyari_kutusu.setText("Seçilen dosyadaki veriler çekiliyor. Lütfen bu işlemler yapılırken bilgisayarda yeni bir işlem başlatmayınız!")
        girilen_esik_deger = self.EsikDegeri.value()
        dosya_yolu  = r'%s' % self.DosyaYolu
        self.yukleniyor(5)
        grf.veri_to_df(dosya_yolu)
        self.yukleniyor(15)
        grf.kumulatif_hesap()
        self.yukleniyor(35)
        grf.eks_log_hesabi()
        self.yukleniyor(50)
        grf.birlestirme_islemi()
        self.uyari_kutusu.setText("...")
        self.yukleniyor(70)
        grf.grafik_ciz(girilen_esik_deger)
        self.uyari_kutusu.setText("Belirlediğiniz eşik değerin üstündeki veriler aranıyor. Bu adım veri sayısına bağlı olarak uzun sürebilir.")
        self.yukleniyor(90)
        grf.esik_deger_tarama(girilen_esik_deger)
        self.uyari_kutusu.setText("Manhattan Plot çizildi.")
        self.yukleniyor(100)
                     
Uygulama = QApplication(sys.argv)
YuklemePenceresiNesnesi = YuklemePenceresi()
YuklemePenceresiNesnesi.show()

Uygulama.exec_()
