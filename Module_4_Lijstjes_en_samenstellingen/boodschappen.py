boodschappen = {}
meerboodschappen = "ja"


while meerboodschappen == "ja":
    vraag = input ("Wil je nogmeer boodschappen toevoegen: ")
    if vraag  == "ja":
        vraag2 = input ("Wat zou je willen toevoegen aan je boodschappenlijst?: ")
        vraag3 = input (f"Hoeveel {vraag2} zou je willen toevoegen?: ")
        boodschappen[vraag2]= vraag3
    else:   
        break
for x in boodschappen:
    print (f"{x} x {boodschappen[x]}")