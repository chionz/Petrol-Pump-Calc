import time
import random
money = input("Input Currency ")
currency = money
funit = "ltrs"
def mode():
    print("Choose Mode")
    print("1. Liters")
    print("2. Price")
    
    global choosemode
    choosemode = int(input("Select mode "))
    global sp
    sp = float(input("Insert Selling Price "))


def chooseprice():
    price = int(input("How much are you buying? "))

    calc = price + 1

    #expected liter
    unit = price / sp
    
    for count in range(0, calc, 1):
        out = count / sp
        print(funit,format(out, "0.3f"), " = ", count,currency)
        time.sleep(0.2)

    print("You will pay",currency,price, "for ",format(unit,"0.2f"),funit)

def chooseliter():
    liter = float(input("Input liter "))

    calc = int(liter) + 1
    
    #expected price
    uprice = liter * sp
    
    for count in range(0, calc, 1):
        out = float(count) * sp
        print(format(out, "0.3f"),currency, " = ", count,funit)
        time.sleep(random.randint(0,1))

    print("You will Pay",currency, format(uprice,"0.2f"), "for ",format(liter,"0.2f"),funit)
    
while True:
    mode()

    if choosemode == 2:
        chooseprice()
        
    if choosemode == 1:
        chooseliter()