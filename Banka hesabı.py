banka_verileri = {
    "TR101": {"bakiye": 1500, "isim": "Ahmet"},
    "TR102": {"bakiye": 2000, "isim": "Ayşe"}
}
#para_yatir(hesap_no, miktar) fonksiyonu yazın.
#Eğer hesap numarası sözlükte varsa, mevcut bakiyesine miktarı eklesin.
#Eğer hesap yoksa, bu hesap numarasını yeni bir kayıt olarak sözlüğe eklesin (Başlangıç bakiyesi olarak girilen miktarı yazarak).
def para_yatir(hesap_no,miktar):
    if hesap_no in banka_verileri:
        banka_verileri[hesap_no]["bakiye"]+=miktar
        print(f"{hesap_no} nolu hesaba {miktar} TL yatırıldı.")
    else:
        banka_verileri[hesap_no] = {"bakiye": miktar, "isim": "Yeni Kayıt"}
        print(f"Yeni hesap ({hesap_no}) oluşturuldu ve {miktar} TL bakiye yüklendi.")
# Testler:
para_yatir("TR101", 1500) # Var olanı günceller
para_yatir("TR103", 5000) # Olmayanı yeni açar (Senin örneğindeki değerler)

print(banka_verileri)