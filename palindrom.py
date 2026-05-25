def palindrom(metin):
    metin=metin.lower()
    return metin==metin[:-1]
print(palindrom("Nalan"))
print(palindrom("Berktug"))
def iki_isaretci_ile_palindrom(metin1):
    temiz_metin="".join (k.lower(0) for k in metin1 if k .isalnum())
    sol=0
    sag=len(temiz_metin)-1
    while sol<sag:
        if temiz_metin[sol] !=temiz_metin[sag]:
            return False
        sol+=1
        sag-=1
    return True
print(iki_isaretci_ile_palindrom("Kacak"))
print(iki_isaretci_ile_palindrom("Can"))
    