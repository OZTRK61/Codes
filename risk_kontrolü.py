def kuvvet_alici(kuvvet):
    """
    Verilen kuvvette alan bir fonksiyon üretir
    """
    def kuvvet_al(sayi):
        return sayi ** kuvvet
    return kuvvet_al

# Kullanım
kare_al = kuvvet_alici(2)
kup_al = kuvvet_alici(3)
dort_kuvvet = kuvvet_alici(4)

print(f"5'in karesi: {kare_al(5)}")
print(f"5'in küpü: {kup_al(5)}")
print(f"5'in 4. kuvveti: {dort_kuvvet(5)}")



def esik_deger_kontrolu(esik):
    """
    Eşik değer kontrolü yapan fonksiyon üretir
    """
    def kontrol(sayi):
        if sayi > esik:
            return f"{sayi}, eşik değer {esik}'den BÜYÜK"
        elif sayi < esik:
            return f"{sayi}, eşik değer {esik}'den KÜÇÜK"
        else:
            return f"{sayi}, eşik değer {esik}'e EŞİT"
    return kontrol

# Kullanım
yuksek_risk_kontrolu = esik_deger_kontrolu(70)
dusuk_risk_kontrolu = esik_deger_kontrolu(30)

print(yuksek_risk_kontrolu(85))
print(yuksek_risk_kontrolu(65))
print(dusuk_risk_kontrolu(25))