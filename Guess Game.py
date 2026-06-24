print("==== Guess The Number Game ===")
print("i have selected a number between 1 to 100")

import random
random.randint(1,100)

jackpot = random.randint(1,100)

try:
 guess = int(input("Guess The Number:"))
except ValueError:
  print("Please Enter Valid Number")

counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")
    
    guess =int(input("Guess The Number:"))
    counter +=1

else:
    print("Your Answer is right, The Number is", guess)
    print("You took ", counter , "attempt")