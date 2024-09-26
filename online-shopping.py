def start():
    who=input("Press p for producer and c for consumer: ")

    if who=="p":
        producer()
    elif who=="c":
        lol=int(input("press '1' for mummy and '2' for dad"))
        if lol==1:
            mummy()
        elif lol==2:
            dad()
    else:
        print("press the valid button")


def main():
    global lower
    global shirt
    global tshirt
    lower=0
    shirt=0
    tshirt=0

def cartim():
    global mlower
    global mshirt
    global mtshirt
    mlower=0
    mshirt=0
    mtshirt=0
    
def cartm():
    global mlower
    global mshirt
    global mtshirt

    print("Lower=",mlower)
    print("Shirt=",mshirt)
    print("Tshirt=",mtshirt)

def ordersm():
    global omlower
    global omshirt
    global omtshirt
    omlower=0
    omshirt=0
    omtshirt=0

def cartip():
    global plower
    global pshirt
    global ptshirt
    plower=0
    pshirt=0
    ptshirt=0

def cartp():
    global plower
    global pshirt
    global ptshirt

    print("Lower=",plower)
    print("Shirt=",pshirt)
    print("Tshirt=",ptshirt)

def ordersp():
    global oplower
    global opshirt
    global optshirt
    oplower=0
    opshirt=0
    optshirt=0

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


def mummy():
    global lower
    global shirt
    global tshirt

    global mlower
    global mshirt
    global mtshirt

    global omlower
    global omshirt
    global omtshirt

    product=input("which product you wanna add to cart PRESS l for lower , s for shirt , t for tshirt, b for buy your cart , o for check your orders:  ")
    if product=="l":
        numm=int(input("no. of lower u wanna buy: "))
        if numm>lower:
            print(numm,"lower are not available")
        else:
            lower-=numm
            print(numm,"lower added to your cart")
            mlower+=numm
            cartview=input("enter anything to continue or enter c to view cart: ")
            if cartview=="c":
                cartm()
            else:
                pass

    elif product=="s":
        num=int(input("no. of shirt u wanna buy: "))
        if num>shirt:
            print(num,"shirt are not available")
        else:
            shirt-=num
            print(num,"shirt added to your cart")
            mshirt+=num
            cartview=input("enter anything to continue or enter c to view cart: ")
            if cartview=="c":
                cartm()
            else:
                pass

    elif product=="t":
        num=int(input("no. of tshirt u wanna buy: "))
        if num>tshirt:
            print(num,"tshirt are not available")
        else:
            lower-=num
            print(num,"tshirt added to your cart")
            mtshirt+=num
            cartview=input("enter anything to continue or enter c to view cart: ")
            if cartview=="c":
                cartm()
            else:
                pass
    elif product=="b":
        cartm()
        yup=input("You Have these items in your cart. press a to buy:" )
        if yup=="a":
            if mlower==0 and mshirt==0 and mtshirt==0:
                print("YOU HAVE TO FIRST ADD SOMETHING TO THE CART TO BUY")
            else:

                print("personal details:-")
                adres=input("enter your address: ")
                phone=input("enter your phone num: ")
                pay=input("enter 'cod' for cash on delivry or enter 'yup' to pay now online: ")
                if pay=="cod":
                    print("you will recieve your order in 5 days at your doorstep.")
                    print("Thanks for buying")
                    omlower=mlower
                    omshirt=mshirt
                    omtshirt=mtshirt
                    mlower=mshirt=mtshirt=0
                elif pay=="yup":
                    print("8008978278 PLEASE PAY THE AMOUNT TO THIS UPI ")
                    print("Thanks for buying")
                    omlower=mlower
                    omshirt=mshirt
                    omtshirt=mtshirt
                    mlower=mshirt=mtshirt=0
        else:
            pass
    elif product=="o":
        print("lower=",omlower)
        print("shirt=",omshirt)
        print("tshirt=",omtshirt)
    else:
        print("wrong input")    

def dad():
    global lower
    global shirt
    global tshirt

    global plower
    global pshirt
    global ptshirt

    global oplower
    global opshirt
    global optshirt

    product=input("which product you wanna add to cart PRESS l for lower , s for shirt , t for tshirt, b for buy your cart , o for check your orders:  ")
    if product=="l":
        num=int(input("no. of lower u wanna buy: "))
        if num>lower:
            print(num,"lower are not available")
        else:
            lower-=num
            print(num,"lower added to your cart")
            plower+=num
            cartview=input("enter anything to continue or enter c to view cart: ")
            if cartview=="c":
                cartp()
            else:
                pass

    elif product=="s":
        num=int(input("no. of shirt u wanna buy: "))
        if num>shirt:
            print(num,"shirt are not available")
        else:
            shirt-=num
            print(num,"shirt added to your cart")
            pshirt+=num
            cartview=input("enter anything to continue or enter c to view cart: ")
            if cartview=="c":
                cartp()
            else:
                pass

    elif product=="t":
        num=int(input("no. of tshirt u wanna buy: "))
        if num>tshirt:
            print(num,"tshirt are not available")
        else:
            lower-=num
            print(num,"tshirt added to your cart")
            ptshirt+=num
            cartview=input("enter anything to continue or enter c to view cart: ")
            if cartview=="c":
                cartp()
            else:
                pass
    elif product=="b":
        cartp()
        yup=input("You Have these items in your cart. press a to buy:" )
        if yup=="a":
            if plower==0 and pshirt==0 and ptshirt==0:
                print("YOU HAVE TO FIRST ADD SOMETHING TO THE CART TO BUY")
            else:

                print("personal details:-")
                adres=input("enter your address: ")
                phone=input("enter your phone num: ")
                pay=input("enter 'cod' for cash on delivry or enter 'yup' to pay now online: ")
                if pay=="cod":
                    print("you will recieve your order in 5 days at your doorstep.")
                    print("Thanks for buying")
                    oplower=plower
                    opshirt=pshirt
                    optshirt=ptshirt
                    plower=pshirt=ptshirt=0
                elif pay=="yup":
                    print("8008978278 PLEASE PAY THE AMOUNT TO THIS UPI ")
                    print("Thanks for buying")
                    oplower=plower
                    opshirt=pshirt
                    optshirt=ptshirt
                    plower=pshirt=ptshirt=0
        else:
            pass
    elif product=="o":
        print("lower=",oplower)
        print("shirt=",opshirt)
        print("tshirt=",optshirt)
    else:
        print("wrong input")

ordersp()
cartip()

ordersm()
cartim()

main()
start()
a=int(input("press 0 to continue shopping: "))
i=0
while i<1:
    if a == 0:
        start()
    else:
        print("exited")
    i=a
    
