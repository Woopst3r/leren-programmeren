# Een spelletje kost in de winkel 24,95, maar gamewinkels krijgen 40% korting bij inkoop. 
# Het versturen vanuit de leverancier kost 1,00 voor het eerset spel, en 25 cent voor ieder volgnde game. 
# Bereken hoeveel de gamewinkel betaalt voor 60 spelletje.


PRIJSSPEL = 24.95
KORTING = 0.6


def game(aantal):
    return ((aantal - 1*0.25)+1) + ((PRIJSSPEL * KORTING) * aantal)  
print(game(60))