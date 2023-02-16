import random

namen = []



while True:
    vraag_namen = input ("Geef mij een naam: ").lower()
    if vraag_namen in namen:
        print("Het moet verschillende namen zijn.")
    else:
        namen.append(vraag_namen)
    print(namen)
    if len (namen) >= 3:
        nogmeer_namen = input ("Wil je nog meer namen toevoegen?: ")
        if nogmeer_namen == ("nee"):
            break

lootjes = namen.copy()

dictionary_lijst = []

while namen:
    if namen[0] != lootjes[0]:
        dictionary_lijst.append({namen[0]: lootjes[0]})
        del namen[0]
        del lootjes[0]
    else:
        random.shuffle(lootjes)

print (dictionary_lijst)







