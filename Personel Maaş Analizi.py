#maaşı en yüksek olan kişiyi ve maaşını bulan kodu yazın.
personeller = {
    "Ahmet": {"maas": 25000, "bolum": "IT"},
    "Canan": {"maas": 32000, "bolum": "IK"},
    "Selin": {"maas": 28000, "bolum": "Satis"}
}

def en_yuksek_maasli_bul():
    en_yuksek_maas = 0
    en_yuksek_maasli_personel = ""

    for isim in personeller:
        # Önce isme gidiyoruz, sonra onun altındaki maaşa
        su_anki_maas = personeller[isim]["maas"]
        
        if su_anki_maas > en_yuksek_maas:
            en_yuksek_maas = su_anki_maas
            en_yuksek_maasli_personel = isim
    
    # Döngü bitti, artık en büyüğü biliyoruz:
    print(f"En çok maaş alan: {en_yuksek_maasli_personel} ({en_yuksek_maas} TL)")

en_yuksek_maasli_bul()