Name=(input("enter your name : "))
Gender=(input("enter your gender: "))
age=int(input("enter your age: "))
m="male"
f="female"

product=(input("enter product name: "))
Gram=float(input("enter a gram: "))
goldprice=9786
print("today GOLD price(1 gram) = ",goldprice)

print("---------------------------------------------------------------")

print("your total gold price is = ",Gram*goldprice)
totalgold=Gram*goldprice
print("Making charges ( 1 gram ) = 845")
totalmakingcharge=Gram*845
print("total making charge =",totalmakingcharge)
print("-----------------------------------------------------------------")

totalamount=totalgold+totalmakingcharge
print("you total amount is : ",totalamount)
print("shopping upto 2 lakh+ and get special discounts on product")

if Gender == m and age >=65:
    if totalamount >=200000 and totalamount <300000:
        print("You are Getting discount = ",totalamount*0.20)
        print("Your total net amount = ", totalamount - (totalamount*0.20))
    if totalamount >=300000 and totalamount <500000:
        print("You are Getting discount = ",totalamount*0.30)
        print("Your total net amount = ", totalamount - (totalamount*0.30))
    if totalamount >=500000:
        print("You are Getting discount = ",totalamount*0.35)
        print("Your total net amount = ", totalamount - (totalamount*0.35))
elif Gender == m and age <65:
    if totalamount >=200000 and totalamount <300000:
        print("You are Getting discount = ",totalamount*0.10)
        print("Your total net amount = ", totalamount - (totalamount*0.10))
    if totalamount >=300000 and totalamount <500000:
        print("You are Getting discount = ",totalamount*0.20)
        print("Your total net amount = ", totalamount - (totalamount*0.20))
    if totalamount >=500000:
        print("You are Getting discount = ",totalamount*0.25)
        print("Your total net amount = ", totalamount - (totalamount*0.25))
elif Gender == f and age >=65:
    if totalamount >=200000 and totalamount <300000:
        print("You are Getting discount = ",totalamount*0.25)
        print("Your total net amount = ", totalamount - (totalamount*0.25))
    if totalamount >=300000 and totalamount <500000:
        print("You are Getting discount = ",totalamount*0.35)
        print("Your total net amount = ", totalamount - (totalamount*0.35))
    if totalamount >=500000:
        print("You are Getting discount = ",totalamount*0.40)
        print("Your total net amount = ", totalamount - (totalamount*0.40))
elif Gender == f and age <65:
    if totalamount >=200000 and totalamount <300000:
        print("You are Getting discount = ",totalamount*0.15)
        print("Your total net amount = ", totalamount - (totalamount*0.15))
    if totalamount >=300000 and totalamount <500000:
        print("You are Getting discount = ",totalamount*0.25)
        print("Your total net amount = ", totalamount - (totalamount*0.25))
    if totalamount >=500000:
        print("You are Getting discount = ",totalamount*0.30)
        print("Your total net amount = ", totalamount - (totalamount*0.30))
else:
    print("Invalid Input")              