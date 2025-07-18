import random

print("Level 1: Guess the number between 1 and 100")
comp = random.randint(1, 100)

while True:
    user = int(input("Enter a number: "))
    if user > comp:
        print("Guess lower number")
    elif user < comp:
        print("Guess higher number")
    else:
        print(" RIGHT GUESS !!! You passed Level 1!")
        break  

print(" Level 2: Guess the number between 1 and 50")
print("You have 7 attempts to guess the number.")
comp1 = random.randint(1, 50)
level2 = False

for i in range(1, 8):
    user = int(input("Enter a number: "))
    if user > comp1:
        print("Guess lower number")
    elif user < comp1:
        print("Guess higher number")
    else:
        print(" RIGHT GUESS !!! You passed Level 2!"

