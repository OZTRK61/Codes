#Aynı harflerin yan yana kaç kez tekrarlandığını bulan döngü kur.
kelime=input("bir kaç kelime giriniz:")
a_sayacı=0
b_sayacı=0
c_sayacı=0
for harf in kelime:
    if kelime=='a':
        a_sayacı+=1
    if kelime=='b':
        b_sayacı+=1
    if kelime=='c':
        c_sayacı+=1
print(f"a harfinden:{a_sayacı} kadar var,b harfinden:{b_sayacı} kadar var,c harfinden:{c_sayacı} kadar var.")