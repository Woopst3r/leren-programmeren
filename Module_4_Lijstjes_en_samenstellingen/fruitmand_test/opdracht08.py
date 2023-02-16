from fruitmand import fruitmand
watermeloen = {
    'name' : 'watermelon',
    'weight' : 900,
    'color' : 'green',
    'round' : True
    }

fruitmand.append(watermeloen)

for fruit in (fruitmand):
    print (fruit['weight'])
