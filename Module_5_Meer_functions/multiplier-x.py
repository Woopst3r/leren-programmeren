berekening = int(input("Van welk getal wilt u de tafel zien?:"))

def vraag(nummer):
    for tafels in range (1, 11):   
        print (f"{tafels} x {nummer} = {tafels*nummer}")


vraag(berekening)