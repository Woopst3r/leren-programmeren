import random

kleuren = {"oranje","blauw","groen","bruin"}
zak = []
vraag = int(input ("Hoeveel M%M moet er aan de zak toegevoed worden: "))


while vraag >= 0:
    #list . voeg toe: random getal in kleuren
    zak.append(kleuren[random.randint(0,3)])
    vraag -= 1
print (f"Dit zijn de m&m in de zak: {zak}")

