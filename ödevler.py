ogrenciler={
 "Ali":("Matematik",[80,90,70]),
 "Ayşe":("Fizik",[55,45,35]),
"Mehmet":("Kimya",[100,20,30]),
"Ahmet":("Matematik",[60,20,100]),
"Ömer":("Fizik",[35,35,35]),
"Fatma":("Kimya",[85,65,75]),
}
#sınıf ortalamasını bul
toplam_not=0
not_sayisi=0
for veri in ogrenciler.values():
    notlar=veri[1]
    toplam_not=sum(notlar)
    not_sayisi=len(notlar)
    sınıf_ortalaması=toplam_not/not_sayisi
    print(f"Sınıfın Genel Ortalaması: {sınıf_ortalaması:.2f}")
#1.sınav ortalamasını bul
birinci_sinav_notlari = [veri[1][0] for veri in ogrenciler.values()]
birinci_sinav_ortalamasi = sum(birinci_sinav_notlari) / len(birinci_sinav_notlari)
print(f"1. Sınav Notları: {birinci_sinav_notlari}")
print(f"1. Sınav Ortalaması: {birinci_sinav_ortalamasi:}")
#ödev ortalamasını bulun
ödev_notlari = [veri[1][1] for veri in ogrenciler.values()]
ödev_ortalamasi=sum(ödev_notlari)/len(ödev_notlari)
print(f"ödev notlari:{ödev_notlari}")
print(f"ödev ortalamasi:{ödev_ortalamasi:}")
#final ortalamasını bulun
final_notlari=[veri[1][2] for veri in ogrenciler.values()]
final_ortalamasi=sum(final_notlari)/len(final_notlari)
print(f"final notlari:{final_notlari}")
print(f"final ortalamasi:{final_ortalamasi}")
#cinsiyete göre hesaplama
erkekler = ["Ali", "Mehmet", "Ahmet", "Ömer"]
kizlar = ["Ayşe", "Fatma"]

erkek_not_toplami = 0
erkek_sayisi = 0

for isim, veri in ogrenciler.items():
    if isim in erkekler:
        erkek_not_toplami += sum(veri[1]) 
        erkek_sayisi += len(veri[1])

print(f"Erkeklerin Genel Ortalaması: {erkek_not_toplami / erkek_sayisi:}")

vize_notlari=[veri[1],[2] for veri in ogrenciler.values()]
vize_ortalamasi=sum(vize_notlari)/len(vize_notlari)
print(f"Vize notları:{vize_notlari}")
print(f"vize ortlamasi:{vize_ortalamasi}")
