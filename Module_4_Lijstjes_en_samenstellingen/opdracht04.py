import random
from fruitmand import fruitmand

aantal = int(input("Hoeveel fruit wil je?"))
for x in range(aantal):   
    random_fruit = random.choice(fruitmand)
    print (random_fruit['name'])

