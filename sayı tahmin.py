import random

low=1
high=100
guesses=0
number=random.randint(low,high)

while True:
 guess=int(input(f"enter a between number({low}-{high}):"))
 guesses+=1

 if guess<number:
  print(f"{guess} to low")
 elif guess>number:
  print(f"{guess} to high")
 else:
  print(f"{guess} correct")
  break

 print(f"this round took you {guesses} guesses")