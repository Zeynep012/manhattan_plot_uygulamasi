from yukleme_arayuz import Ui_MainWindow as YuklemeArayuz
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog
from PyQt5 import QtWidgets
from openpyxl import load_workbook
import sys
import grafik as grf

class YuklemePenceresi(QMainWindow, YuklemeArayuz):
    def __init__(self):
        super().__init__()
        self.DosyaYolu = ''
        self.basla()
    
    def basla(self):
        self.setupUi(self)
        self.Aktar.clicked.connect(self.AktarFonk)
        self.manPlot.clicked.connect(self.grafik_cizdir)
       
    def DosyaSec(self):
        self.dosya_iletisim = QFileDialog(self)
        self.dosya_ac = self.dosya_iletisim.getOpenFileName(self,"Dosya Ac")
        return self.dosya_ac[0]
    
    def AktarFonk(self):
        self.DosyaYolu = self.DosyaSec()
        
    def grafik_cizdir(self):
        girilen_esik_deger = self.EsikDegeri.value()
        dosya_yolu  = r'%s' % self.DosyaYolu
        grf.grafik(dosya_yolu,girilen_esik_deger)
    
                                
Uygulama = QApplication(sys.argv)
YuklemePenceresiNesnesi = YuklemePenceresi()
YuklemePenceresiNesnesi.show()

Uygulama.exec_()



