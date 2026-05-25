
i̇lginc=([ -2, 33, 14, 6, - -13, 9, 2])
def ilginc_hale_getir(num_list):
    yeni=[]
    for sayılar in num_list:
        if sayılar>=0:
            if sayılar%2==1:
                yeni.append(sayılar+10)
            else:
             yeni.append(sayılar)
        else:
            yeni.append(sayılar)
    return yeni
print(ilginc_hale_getir(i̇lginc))


# 1. Kullanıcıdan kaç öğrenci girileceğini alıyoruz
ogrenci_sayisi = int(input("Kaç öğrenci bilgisi gireceksiniz?: "))

isimler = []
notlar = []

# 2. Bilgileri tek tek listelere ekliyoruz
for i in range(ogrenci_sayisi):
    ad_soyad = input(f"{i+1}. Öğrencinin Adı ve Soyadı: ")
    notu = input(f"{i+1}. Öğrencinin Notu: ")
    
    isimler.append(ad_soyad)
    notlar.append(notu)

# 3. Boş bir sözlük oluşturup döngü ile dolduruyoruz (zip kullanmadan)
ogrenci_sozlugu = {}

for i in range(len(isimler)):
    # Her bir indeksteki ismi anahtar, notu değer olarak atıyoruz
    ogrenci_sozlugu[isimler[i]] = notlar[i]

# 4. Sonucu ekrana yazdırıyoruz
print("\nOluşturulan Öğrenci Not Sözlüğü:")
print(ogrenci_sozlugu)