import random
Nummerkaart = ("2","3","4","5","6","7","8","9","10","boer","vrouw","koning","aas")
Kaartsoort = ("Klaver","Harten","Schoppen","Ruiten")
deck = []
teller = 0

deck.append("Joker1")
deck.append("Joker2")
for x in Nummerkaart:
    for y in Kaartsoort:
        deck.append(f"{y} {x}")

random.shuffle(deck)
print (deck)

for x in range (1,8):
    teller+=1
    print (f"Kaart {teller} : {deck.pop(0)}")
print (deck)