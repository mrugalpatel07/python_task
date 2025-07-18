shop={}
print("welcome to shop")
while True:
    print("1. manager")
    print("2. customer")
    ch=int(input("enter: "))
    if ch==1:
        n=input("item name: ")
        q=int(input("qty: "))
        p=int(input("price: "))
        if n in shop:
            shop[n]["qty"]=shop[n]["qty"]+q
            shop[n]["price"]=p
        else:
            shop[n]={"qty":q,"price":p}
        print("items:")
        for i in shop:
            print(i,shop[i]["qty"],"pcs",shop[i]["price"],"rs")
    elif ch==2:
        if shop=={}:
            print("no stock")
            continue
        print("items:")
        for i in shop:
            print(i,shop[i]["price"],"rs")
        total=0
        bill=[]
        while True:
            n=input("buy item: ")
            if n not in shop:
                print("not found")
                continue
            q=int(input("qty: "))
            if q>shop[n]["qty"]:
                print("only",shop[n]["qty"],"left")
                continue
            price=shop[n]["price"]
            total=total+(q*price)
            bill.append((n,q,price))
            shop[n]["qty"]=shop[n]["qty"]-q
            more=input("more? y/n: ")
            if more!="y":
                break
        print("bill:")
        for i in bill:
            print(i[0],i[1],"x",i[2],"=",i[1]*i[2])
        print("total:",total)