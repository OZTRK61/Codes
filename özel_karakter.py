metin = "Kodlama_123!"
ozel_karakter_sayisi=0
for karakter in metin:
    if not karakter.isalnum():
        ozel_karakter_sayisi+=1
print(f"özel karakter sayisi:{ozel_karakter_sayisi}")
#fonksiyonu, karakterin harf veya rakam olup olmadığını kontrol eder. 
# Eğer ikisi de değilse, onu "özel" olarak kabul eder ve sayacı artırır.
