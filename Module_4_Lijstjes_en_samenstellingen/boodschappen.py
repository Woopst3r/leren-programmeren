boodschappenlijst = {}
meerboodschappen = "ja"


while meerboodschappen == "ja":

    boodschap = input ("Wat zou je willen toevoegen aan je boodschappenlijst?: ").lower()
    aantal = input (f"Hoeveel {boodschap} zou je willen toevoegen?: ").lower()
    boodschappenlijst[boodschap]= aantal
    if boodschap in boodschappenlijst:
        boodschappenlijst[boodschap] += aantal
    else:
        boodschappenlijst[boodschap] = 1


    meerboodschappen = input ("Wil je nogmeer boodschappen toevoegen: ")      

for x in boodschappenlijst:
    print (f"{x} x {boodschappenlijst[x]}")