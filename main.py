# @author: Zeynep Demirtaş

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
        self.uygulama_kulavuzu = "Manhattan grafiğini çizdirmek için önce verileriniz olduğu dosyayı seçiniz. Daha sonra eşik değeri girip 'MANHATTAN PLOT'  butonuna tıklayınız."
        self.basla()
    
    def basla(self):
        try:
            self.setupUi(self)
            self.pb_grafik_cizimi.setValue(0)
            self.Aktar.clicked.connect(self.AktarFonk)
            self.manPlot.clicked.connect(self.grafik_cizdir)
        except Exception as hata :
            self.uyari_kutusu.setText(hata)
       
    def DosyaSec(self):
        try:
            self.dosya_iletisim = QFileDialog(self)
            self.dosya_ac = self.dosya_iletisim.getOpenFileName(self,"Dosya Ac")
            return self.dosya_ac[0]
        except Exception as hata :
            self.uyari_kutusu.setText(hata)
    
    def uzanti_bul(self,dosya):
        try:
            k = 0
            kntrl = False
            uzanti = []
            for i,parca in enumerate(dosya):
            #bu dosya yolunun sonundaki dosyanin uzantisini ayiran dongu
                if parca == '.' or kntrl == True:
                    kntrl = True
                    uzanti.insert(k,dosya[i])
                    k += 1
            return uzanti
        except Exception as hata :
            self.uyari_kutusu.setText(hata)
    
    def AktarFonk(self):
        try:
            self.DosyaYolu = self.DosyaSec()
            if self.DosyaYolu == "":
                self.uyari_kutusu.setText("DOSYA SEÇİMİ YAPILMADI veya BİR HATA YAŞANDI! \n" + self.uygulama_kulavuzu)
            elif self.uzanti_bul(self.DosyaYolu) != ['.', 'x', 'l', 's', 'x']:
                self.uyari_kutusu.setText("SEÇTİĞİNİZ DOSYA 'xlsx' UZANTILI OLMALIDIR! \n" + self.uygulama_kulavuzu)
            else:
                self.uyari_kutusu.setText("Şimdi eşik değerini girip grafiği çizdirebilirsiniz.")
        except Exception as hata :
            self.uyari_kutusu.setText(hata)
            
    def yukleniyor(self,ilerleme_degeri):
        try:
            self.pb_grafik_cizimi.setValue(ilerleme_degeri)
        except Exception as hata :
            self.uyari_kutusu.setText(hata)
        
    def grafik_cizdir(self):
        try:
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
        except Exception as hata :
            self.uyari_kutusu.setText(hata)
                     
Uygulama = QApplication(sys.argv)
YuklemePenceresiNesnesi = YuklemePenceresi()
YuklemePenceresiNesnesi.show()

Uygulama.exec_()
