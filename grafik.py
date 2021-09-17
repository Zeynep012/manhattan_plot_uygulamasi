# @author: Zeynep Demirtaş

import pandas
import seaborn
import numpy
from adjustText import adjust_text
import matplotlib.pyplot as plt

#Hazirlik islemleri
cumulative_pos = []
ekslog = []

def veri_to_df(dosya):
    #Verilerin oldugu dosyayi Data Frame'e donusturme
    global df
    df = pandas.read_excel(dosya)

def kumulatif_hesap():
    baslangic = 0
    #Her bir kayit icin pozisyonlarin kumulatif hesabı
    for chrom,digerleri in df.groupby('Chr_id'):
        cumulative_pos.append(digerleri['Start']+baslangic)
        baslangic += digerleri['Start'].max()

def eks_log_hesabi():
    #Pozisyon degerlerinin -log10 tabaninda degerlerini hesaplama
    veri_uzunlugu = df['Chr_id'].count()
    for indx in range(veri_uzunlugu):
        ekslog.append( -1*numpy.log10(df['Pdegeri'][indx]))

def birlestirme_islemi():
    #Verilerin bulundugu data frame'e iki yeni sutun ekledik.
    #Biri kumulatif pozisyon degerleri, digeri pozisyon degerlerinin -log10 tabanindaki degerleri
    df['cumulative_pos'] = pandas.concat(cumulative_pos)
    df['ekslog'] = ekslog 
    
def grafik_ciz(esikDeger):
    #Grafik çizdirme islemi
    global graf
    graf = seaborn.relplot(data=df, x ='cumulative_pos', y='ekslog',hue='Chr_id',aspect=3, palette = 'Set1')
    graf.ax.axhline(esikDeger,linestyle = '--',linewidth=1)#Esik degerini cizdirme
    graf.ax.set_ylabel('-log10')

def esik_deger_tarama(esikDeger):
    #Esik degerin ustunde olanlarin  bilgilerini yazdirma
    bilgiler = df[df['ekslog'] > esikDeger].apply(lambda p : graf.ax.annotate(p['AxiomKodu'], (p['cumulative_pos'], p['ekslog'])), axis=1).to_list()
    adjust_text(bilgiler)
    
    plt.show()
