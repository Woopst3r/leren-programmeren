print("""
       ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
       +          SollicitatieFormulier "ruimtevuilisman        +
       ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
       We gaan je een paar vragen stellen om meer te komen te ko-
       men teweten over jouw. Als je aan de criteria voldoet.
       is er een mogelijkheid dat je bij ons een ruimtevulisman
       kan worden. De vragen starten nu.                         
       ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
naam = (input("Wat is u naam? : "))
leeftijd = int(input("Wat is jouw leeftijd?: "))
geslacht = input("Wat is jouw geslacht? m/v:  ")
if geslacht == "m":
    snor= input("Heeft u een snor? j/n: ")
    if snor == "j": 
        snor_lengte = int(input("Hoe breed is je snor in cm?: "))
else:
    rood = input("Heeft u rood haar? j/n: ")
    if rood == "j":
        krul_lengte = int(input("Hoe lang is u haar in cm?: "))
lengte = int(input("What is u lengte in cm?: "))
gewicht = int(input("What momenteel u gewicht?: "))
certificaat = input("heeft u een certificaat Overleven met gevaarlijk personeel? j/n: ")
dieren_dressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?: "))
jongleren = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren?: "))
acrobatiek = int(input("Hoeveel jaar praktijkervaring heeftu met acrobatiek?: "))

if (geslacht == "m" and snor_lengte >= 10 and snor_lengte <= 20)or(geslacht == "v" and rood == "j" and krul_lengte >= 20) and leeftijd >= 22 and leeftijd <= 50 and lengte >= 150 and lengte <= 220 and gewicht >= 90 and gewicht <= 120 and certificaat == "j" and(dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3):
    print ("Je bent aangenomen!!")
else:  
    print("Je bent niet aangenomen. :(")
