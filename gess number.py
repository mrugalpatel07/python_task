import random
print("level 1")
print("slect a number between 1 to 100")

num=random.randint(1, 100)

while True:
    gess = int(input("Enter your number: "))
    
    if gess > num:
        print("enter small number")
    elif gess < num:
        print("enter big number")
    else:
        print("win level 1")
        break

print("\nstart level 2")
print("Guess a number between 1 to 50")
print("You have 7 atmp.")

num=random.randint(1, 50)
level2_pass = False

for chance in range(1, 8):
    guess=int(input("enter number = "))
    
    if guess>num:
        print("enter smallnumber")
    elif guess<num:
        print("enter big number")
    else:
        print("win level 2")
        level2_pass=True
        break

if level2_pass:
    print("start level 3")
    print("Gess number between 1 to 100")
    print("You have only 5 chances.")

    num=random.randint(1,100)

    for chance in range(1,6):
        gess=int(input("enter number = "))
        
        if gess>num:
            print("enter small number")
        elif gess<num:
            print("enter big number")
        else:
            print("win level 3")
            print("game over")
            break
    else:
        print("fail level 3.")
else:
    print("fail level 2.")
