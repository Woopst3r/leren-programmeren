aantal_toegangtickets = int(input("Met hoeveel ben je?"))

vr_tijd = int(input("Hoe veel persiodes zou je willen vr spelen?"))




toegangs_ticket = 7.45
vrgamer_5min = 0.37

prijs = (toegangs_ticket * aantal_toegangtickets) + (vr_tijd * vrgamer_5min * aantal_toegangtickets)

print (f"Dit geweldige dagje-uit met {aantal_toegangtickets} mensen in de Speelhal met {vr_tijd} minuten VR kost je maar:", round(prijs, 2))