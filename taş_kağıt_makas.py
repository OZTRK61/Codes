"""
taş kağıt makası fonksiyon ile yap


"""
import random

def tas_kagit_makas():
    skor_oyuncu = 0
    skor_bilgisayar = 0

    while True:
        oyuncu = input("Seçiminizi yapın (taş/kağıt/makas) veya çıkmak için 'q': ").strip().lower()
        if oyuncu == "q":
            print("Oyun bitti!")
            print(f"Son skor: Oyuncu: {skor_oyuncu}, Bilgisayar: {skor_bilgisayar}")
            break

        sayi = random.randint(1, 3)
        if sayi == 1:
            bilgisayar = "taş"
        elif sayi == 2:
            bilgisayar = "kağıt"
        else:
            bilgisayar = "makas"

        if oyuncu == bilgisayar:
            print("Berabere!")
        elif (oyuncu == "taş" and bilgisayar == "makas"):
            print("Kazandınız!")
            skor_oyuncu += 1
        elif  (oyuncu == "kağıt" and bilgisayar == "taş"):
            print("Kazandınız!")
            skor_oyuncu += 1
        elif (oyuncu == "makas" and bilgisayar == "kağıt"):
            print("Kazandınız!")
            skor_oyuncu += 1
        elif oyuncu in ["taş", "kağıt", "makas"]:
            print("Kaybettiniz!")
            skor_bilgisayar += 1
        else:
            print("Geçersiz seçim!")

        print(f"Skor -> Oyuncu: {skor_oyuncu}, Bilgisayar: {skor_bilgisayar}\n")
tas_kagit_makas()