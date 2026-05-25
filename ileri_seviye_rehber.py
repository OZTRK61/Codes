# İç içe geçmiş (nested) sözlük yapısı
rehber = {
    "Ali": {
        "numara": "0530-111-2233",
        "email": "ali@mail.com",
        "dogum_yili": 1995
    },
    "Ayşe": {
        "numara": "0540-444-5566",
        "email": "ayse@mail.com",
        "dogum_yili": 1998
    }
}

# Ali'nin sadece e-posta adresine ulaşmak:
print(rehber["Ali"]["email"]) # Çıktı: ali@mail.com


def detayli_kisi_ekle(isim, numara, email, dogum_yili):
    rehber[isim] = {
        "numara": numara,
        "email": email,
        "dogum_yili": dogum_yili
    }
    print(f"{isim} tüm bilgileriyle kaydedildi.")

# Yeni bir kayıt ekleyelim
detayli_kisi_ekle("Can", "0500-000-1122", "can@web.com", 2000)


def rehberi_dok():
    print("--- DETAYLI REHBER LİSTESİ ---")
    for isim, bilgiler in rehber.items():
        print(f"\nKişi: {isim}")
        print(f"  > Telefon: {bilgiler['numara']}")
        print(f"  > E-posta: {bilgiler['email']}")
        print(f"  > Doğum Yılı: {bilgiler['dogum_yili']}")

rehberi_dok()