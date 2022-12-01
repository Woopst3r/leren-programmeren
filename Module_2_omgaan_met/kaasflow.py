geel = input ("Is de kaas geel? (ja/nee): ")
if geel == "ja":
    gaten = input("Zitten er gaten in? (ja/nee):  ")
    if gaten == "ja":
        duur = input("Is de kaas belagelijk duur? (ja/nee):  ")
        if duur == "ja":
            print ("Emmenthaler")
        elif duur == "nee":
            print ("Leerdammer")
    if gaten == "nee":
        hard = input("Is de kaas hard als steen? (ja/nee):  ")
        if hard == "ja":
            print ("Parmigiano")
        elif hard == "nee":
            print ("Goudse Kaas")
if geel == "nee":
    schimmel = input("Heeft de kaas blauwe schimmel? (ja/nee):  ")
    if schimmel == "ja":
        korst = input("Heeft de kaas een korst? (ja/nee):  ")
        if korst == "ja":
            print ("Blue de Rochbaron")
        elif korst == "nee":
            print ("Foume d'Ambert")
    if schimmel == "nee":
        korst_twee = input("Heeft de kaas een korst? (ja/nee):  ")
        if korst_twee == "ja":
            print ("Camembert")
        elif korst_twee == "nee":
            print ("Mozzarella")
        



        

        




