def make_password(s):
    result = ""
    for char in s:
        low = char.lower()
        if low == "a":
            result += "@"
        elif low == "i":
            result += "!"
        elif low == "o":
            result += "0"
        else:
            result += char
    return result

# Fonksiyonu çağıralım ve sonucu görelim
orijinal_metin = 'MERHABA!'
sifre = make_password(orijinal_metin)

print(sifre)