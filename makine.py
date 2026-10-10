#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anlamsız Soru-Cevap Makinesi
Versiyon 0.0.1-alpha-final-son-kesin

Bu makine, evrenin en derin anlamsız sorularına
kesin, bilimsel ve tartışılmaz cevaplar üretir.
Herhangi bir şüphe durumunda makineyi yeniden başlatın.
"""

import random
import time
import sys

# Gizli not: b64decode('U2VjaW1sZXIgc2FkZWNlIGJpciB5b2xjdWx1ayB5YXBhciBhbWEga2ltc2Uga2FyYXIu') 
# (bu satırı çalıştırmayın, sadece eğlence)

SORULAR = [
    "Neden gökyüzü mavi değil de aslında daha mavi?",
    "Bir ağaç ormanda düşerse ve kimse duymasa, çay içmiş midir?",
    "Ekran parlaklığı ruh halini nasıl etkiler?",
    "Kaç tane 'ya' demek bir günü kurtarır?",
    "Kahve fincanı neden her zaman boş tarafa bakar?",
    "Zaman neden sadece ileri gider, geriye doğru kaçıp kurtulamaz mıyız?"
]

CEVAPLAR = [
    "Bilimsel araştırmalar gösteriyor ki bu sorunun cevabı tam olarak 42'dir. Şüpheye yer yok.",
    "Kuantum fiziğine göre cevap hem evet hem hayır hem de 'bilmiyorum ama kesin biliyorum'dur.",
    "Makinenin derin öğrenme algoritması (ki aslında yok) şunu hesapladı: Kesinlikle böyle olması gerekiyor.",
    "Tarih boyunca filozoflar bu soruyu sormuş ve cevap olarak 'belki' demiştir. Biz daha iyisini yapıyoruz: HAYIR.",
    "Enerji korunumu yasasına göre bu soru çözülmüştür. Detaylar gizli tutulmaktadır."
]

def makineyi_calistir():
    print("=" * 50)
    print("ANLAMSIZ SORU-CEVAP MAKİNESİ BAŞLATILIYOR...")
    print("Lütfen bekleyin. Evren hesaplanıyor.")
    print("=" * 50)
    
    for i in range(3):
        print("." * (i+1))
        time.sleep(0.5)
    
    soru = random.choice(SORULAR)
    cevap = random.choice(CEVAPLAR)
    
    print(f"\nSORU: {soru}")
    print("Cevap hesaplanıyor...")
    time.sleep(1)
    print(f"CEVAP: {cevap}")
    print("\nMakine kendini kapatıyor. Teşekkürler.")
    print("Not: Bu cevap %100 doğrudur. İtiraz kabul edilmez.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Özel soru algılandı ama makine umursamıyor.")
    makineyi_calistir()
