coin = None
cents = None

def yummers():
    global coin
    global cents

    if cents is None:
        cents = 0

    coin = int(input("how much money? "))

    if coin == 5 or coin == 10 or coin == 25:
        cents = coin + cents

    else:
        coin = 0
        cents = coin + cents

def goofert():
    global cents

    while cents < 50:
        print (f"amount due: {50 - cents}")
        yummers()

    else:
        print("")
        print(f"change owed: {cents - 50}")
        print("enjoy :3c")

yummers()
goofert()
