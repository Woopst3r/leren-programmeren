from fruitmand import fruitmand

kleuren = []

kleuren = [item['color'] for item in fruitmand]

print (kleuren)
while True:
    vraag_kleur = input("Kies een kleur: ")
    if vraag_kleur in kleuren:
        break
    else:
        print(f"De kleur {vraag_kleur} zit niet in de fruitmand.")
        continue

rond, niet_rond = 0, 0

for i in range(len(fruitmand)):
    kleur = fruitmand[i].get('color')
    if kleur == vraag_kleur:
        if fruitmand[i].get('round'):
            rond+=1
        else:
            niet_rond+=1

if rond > niet_rond:
    print(f"Er zijn {rond} meer ronde vruchten dan niet-ronde vruchten in de kleur {vraag_kleur}.")

elif rond < niet_rond:
    print(f"Er zijn {niet_rond} meer niet-ronde vruchten dan ronde vruchten in de kleur {vraag_kleur}")

else:
    print(f"Er zijn even veel ronde als niet-ronde vruchten ({rond})")