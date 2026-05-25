#Problem: Bir metindeki ünlü harflerin (a, e, ı, i, o, ö, u, ü) sayısını döndüren fonksiyon.
def ünlü_sayısı(metin):
 ünlü="aeıioöuüAEIİOÖUÜ"
 sayaç=0
 for karakter in metin:
    if karakter in ünlü:
      sayaç+=1
 return sayaç
 
print(ünlü_sayısı("Merhaba dünya"))
  


def unluleri_say(metin):
    unluler = "aeıioöuüAEIİOÖUÜ"
    sayac = 0


    
    for karakter in metin:
        if karakter in unluler:
            sayac += 1
    return sayac

print(unluleri_say("Merhaba Dünya"))  # 5