from fruitmand import fruitmand
from operator import itemgetter

langste_naam_fruit = fruitmand[0]

for fruit in fruitmand:
    if len (fruit['name']) > len(langste_naam_fruit['name']):
        langste_naam_fruit = fruit


print(f'De "{langste_naam_fruit["name"]}" heeft {len(langste_naam_fruit["name"])} letters, heeft een {langste_naam_fruit["color"]} kleur en een gewicht van {langste_naam_fruit["weight"]/1000} kg')