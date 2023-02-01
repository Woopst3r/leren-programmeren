import random

kleuren = ("rood","blauw","groen","bruin","geel")
zak = {} #dictionary
aantal_mnm = int(input ("Hoeveel M&M moet er aan de zak toegevoed worden: "))

for x in range(aantal_mnm):   
    kleur = random.choice(kleuren)
    if kleur in zak:
        zak[kleur] += 1
    else:
        zak[kleur] = 1
for key, value in zak.items():
    if value > 0:
        print(key, ":", value)