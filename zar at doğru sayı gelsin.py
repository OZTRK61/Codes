import random
#sayı aralığı belirle sayılar 0 dan büyükse pozitif olsun değilse negatif

sayı=random.randint(-100,100)
print(f"{sayı}")

if sayı<0:
 print("sayınız negatif")
elif sayı==0:
 print("sayınız pozitif yada negatif değil")
else:
 print("sayınız pozitif")


