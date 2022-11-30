aantal_croissantjes = float(input ("Hoe veel croissantjes wil je hebben croissantjes?"))
aantal_stokbroden = float(input ("Hoe veel aantal_stokbroden wil je hebben croissantjes?"))
aantal_korting_bonnen = float(input ("Hoe veel korting_bonnenje heb je?"))

c_prijs = 0.39
s_prijs = 2.78
korting_bonnen = 0.5

prijs = aantal_croissantjes*c_prijs + aantal_stokbroden*s_prijs - korting_bonnen*aantal_korting_bonnen

print (f"De feestlunch bij de bakker voor de {aantal_croissantjes} croissantjes en de {aantal_stokbroden} stokbroden als de {aantal_stokbroden} kortingsbonnen nog geldig zijn kost je!", prijs)