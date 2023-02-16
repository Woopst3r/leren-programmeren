from fruitmand import fruitmand
from operator import itemgetter

zwaarsteFruit = sorted(fruitmand, key=itemgetter('weight'), reverse=True)
for x in range(len(zwaarsteFruit)):
    print(zwaarsteFruit[x]['name'], zwaarsteFruit[x]['weight'], 'gram')