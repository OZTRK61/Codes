#kişi ekleme
#başlangıç rehberimiz
rehber= {
     "Ali": "0530-111-2233",
    "Ayşe": "0540-444-5566"   

}
def kisi_ekleme(isim,numara):
    rehber[isim]=numara
    print(f"{isim} bşarıyla eklendi.")

def kisi_ara(isim):
    #.get() kullanarak hata almadan kontrol ediyoruz
    numara= rehber.get(isim,"Kişi bulunamadı!")
    print(f"{isim} numarası:{numara}")

#Kullanım örnekleri:
kisi_ekleme("Mehmet","0555-999-8877")
kisi_ara("Ali")
kisi_ara("Zeynep")


#kişi silme
rehber = {
    "Ali": "0530-111-2233",
    "Ayşe": "0540-444-5566"
}

def kisi_sil(isim):
    if isim in rehber:
        silinen = rehber.pop(isim)
        print(f"{isim} rehberden silindi. (Numarası: {silinen})")
    else:
        print(f"Hata: {isim} rehberde bulunamadı.")

# Deneme
kisi_sil("Ali")    # Başarılı olacak
kisi_sil("Veli")   # Hata mesajı verecek



#Tüm Rehberi Listeleme
def rehberi_göster():
    if not rehber: #eğer rehber boşsa
        print("Rehber şu an boş.")
    else:
        print("---İletişim Rehberi---")
        for isim,numara in rehber.items():
            print(f"İsim:{isim} Numara:{numara}")

rehberi_göster()