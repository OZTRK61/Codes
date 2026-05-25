bolge_satısları={}
with open("satıslar.txt","r") as f:
    satıslar=f.readlines()[1:]
    for satir in satirlar:
        bolge,urun,miktar,fiyat=satir.strip().split(";")
        toplam_tutar = int(miktar) * int(fiyat)
        # SÖZLÜK MANTIĞI: Bölge daha önce eklenmiş mi?
        if bolge not in bolge_satisları:
            bolge_satisları[bolge] = 0
            # Üzerine ekle
        bolge_satisları[bolge] += toplam_tutar
        print("Bölge Bazlı Satış Raporu:", bolge_satisları)