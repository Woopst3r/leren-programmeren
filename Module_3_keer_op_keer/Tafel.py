nummer = int(input("Welke tafel wil je weten?: "))
for tafels in range (1,11):   
    tafel = tafels * nummer
    print(f"{tafels} * {nummer}= {tafel}")
