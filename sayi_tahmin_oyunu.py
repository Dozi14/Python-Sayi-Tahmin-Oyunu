# -*- coding: utf-8 -*-
"""
@author: Dogus
"""

import random #sayi tahmini
import time #1 sn bekleme icin

print("""
      *************************************
      Sayı Tahmin Oyunu
      1 ile 40 arasında sayıyı tahmin edin.
      *************************************
      """)

rastgele_sayi = random.randint(1,40)
#1-40 arasi rastgele sayi uretir

tahmin_hakki = 8

while True:
    tahmin = int(input("Tahmininiz:"))
    
    if(tahmin < rastgele_sayi):
        time.sleep(1)
        print("Daha yüksek bir sayı söylemelisiniz.")
        tahmin-=1
    elif(tahmin > rastgele_sayi):
        time.sleep(1)
        print("Daha düşük bir sayı söylemelisiniz.")
        tahmin-=1
    else:
        time.sleep(1)
        print("Tebrikler doğru tahmin ettiniz! Sayı:",rastgele_sayi)
        break
    if(tahmin_hakki == 0):
        print("Maalesef haklarınızı tükettiniz. Sayı:", rastgele_sayi)
        break