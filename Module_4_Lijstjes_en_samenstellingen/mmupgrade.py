import random

kleuren = ("rood","blauw","groen","bruin","geel")
zak = {} #dictionary
vraag = int(input ("Hoeveel M&M moet er aan de zak toegevoed worden: "))

while vraag > 0:
    #add a random color to the dictionary
    kleur = kleuren[random.randint(0,len(kleuren)-1)]
    if kleur in zak:
        zak[kleur] += 1
    else:
        zak[kleur] = 1
    vraag -= 1
for key, value in zak.items():
    if value > 0:
        print(key, ":", value)

