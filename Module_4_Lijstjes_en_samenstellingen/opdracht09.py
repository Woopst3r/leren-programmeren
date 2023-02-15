from fruitmand import fruitmand

for i in range(len(fruitmand)):
    if fruitmand[i]['name'] == "druif":
        del fruitmand[i]
        break

for fruit in (fruitmand):
    print (fruit['color'])