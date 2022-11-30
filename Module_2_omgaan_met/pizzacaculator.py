small = int(input ("Hoeveel small pizza's zou je willen hebben?"))
medium = int(input ("Hoeveel midium pizza's zou je willen hebben?"))
large = int(input ("Hoeveel large pizza's zou je willen hebben?"))
kortingbon = int(input ("Hoeveel korting bonnen heeft u?"))

small_price = 4.5
medium_price = 6
large_price = 8 
kortingbon_procent = 5/100


small_total =small_price * small
medium_total =medium_price * medium
large_total =large_price * large

totaal = small_total + medium_total + large_total
korting = kortingbon_procent * kortingbon * totaal
totaal_met_korting = totaal - korting

print("-------------------------------------------")
print(f"{small} small pizza prijs: {small_total}euro")
print(f"{medium} midium pizza prijs: {medium_total}euro")
print(f"{large} large pizza prijs: {large_total}euro")
print(f" totaal prijs: {totaal}euro")
print(f" totaal prijs met korting: {totaal_met_korting}euro")
print("-------------------------------------------")