def start():
    who=input("Press p for producer and c for consumer: ")

    if who=="p":
        producer()
    elif who=="c":
        customer()
    else:
        print("press the valid button")


def main():
    global lower
    global shirt
    global tshirt
    lower=0
    shirt=0
    tshirt=0


def carti():
    global clower
    global cshirt
    global ctshirt
    clower=0
    cshirt=0
    ctshirt=0

def cart():
    global clower
    global cshirt
    global ctshirt

    print("Lower=",clower)
    print("Shirt=",cshirt)
    print("Tshirt=",ctshirt)

def orders():
    global olower
    global oshirt
    global otshirt
    olower=0
    oshirt=0
    otshirt=0

def producer():
    global lower
    global shirt
    global tshirt
    product=input("which product you are adding PRESS l for lower , s for shirt , t for tshirt , z for check the inventory:   ")
    if product=="l":
        num=int(input("no. of lower u wanna input: "))
        lower+=num
        print("no. of lower now=",lower)
    elif product=="s":
        num=int(input("no. of shirt u wanna input: "))
        shirt+=num
        print("no. of shirt now=",shirt)
    elif product=="t":
        num=int(input("no. of tshirt u wanna input: "))
        tshirt+=num
        print("no. of tshirt now=",tshirt)
    elif product=="z":
        print("lower=",lower)
        print("shirt=",shirt)
        print("tshirt=",tshirt)
    else:
        print("wrong input")


def customer():
    global lower
    global shirt
    global tshirt

    global clower
    global cshirt
    global ctshirt

    global olower
    global oshirt
    global otshirt

    product=input("which product you wanna add to cart PRESS l for lower , s for shirt , t for tshirt, b for buy your cart , o for check your orders:  ")
    if product=="l":
        num=int(input("no. of lower u wanna buy: "))
        if num>lower:
            print(num,"lower are not available")
        else:
            lower-=num
            print(num,"lower added to your cart")
            clower+=num
            cartview=input("enter anything to continue or enter c to view cart: ")
            if cartview=="c":
                cart()
            else:
                pass

    elif product=="s":
        num=int(input("no. of shirt u wanna buy: "))
        if num>shirt:
            print(num,"shirt are not available")
        else:
            shirt-=num
            print(num,"shirt added to your cart")
            cshirt+=num
            cartview=input("enter anything to continue or enter c to view cart: ")
            if cartview=="c":
                cart()
            else:
                pass

    elif product=="t":
        num=int(input("no. of tshirt u wanna buy: "))
        if num>tshirt:
            print(num,"tshirt are not available")
        else:
            lower-=num
            print(num,"tshirt added to your cart")
            ctshirt+=num
            cartview=input("enter anything to continue or enter c to view cart: ")
            if cartview=="c":
                cart()
            else:
                pass
    elif product=="b":
        cart()
        yup=input("You Have these items in your cart. press a to buy:" )
        if yup=="a":
            if clower==0 and cshirt==0 and ctshirt==0:
                print("YOU HAVE TO FIRST ADD SOMETHING TO THE CART TO BUY")
            else:

                print("personal details:-")
                adres=input("enter your address: ")
                phone=input("enter your phone num: ")
                pay=input("enter 'cod' for cash on delivry or enter 'yup' to pay now online: ")
                if pay=="cod":
                    print("you will recieve your order in 5 days at your doorstep.")
                    print("Thanks for buying")
                    olower=clower
                    oshirt=cshirt
                    otshirt=ctshirt
                    clower=cshirt=ctshirt=0
                elif pay=="yup":
                    print("8008978278 PLEASE PAY THE AMOUNT TO THIS UPI ")
                    print("Thanks for buying")
                    olower=clower
                    oshirt=cshirt
                    otshirt=ctshirt
                    clower=cshirt=ctshirt=0
        else:
            pass
    elif product=="o":
        print("lower=",olower)
        print("shirt=",oshirt)
        print("tshirt=",otshirt)
    else:
        print("wrong input")
orders()
main()
carti()
start()
a=int(input("press 0 to continue shopping: "))
i=0
while i<1:
    if a == 0:
        start()
    else:
        print("exited")
    i=a
