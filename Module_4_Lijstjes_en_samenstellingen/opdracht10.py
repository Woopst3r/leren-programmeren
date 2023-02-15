from fruitmand import fruitmand

sorted_list = sorted(fruitmand, key=lambda k: k['weight'], reverse=True)

for fruit in sorted_list:
    print(fruit['weight']/1000)