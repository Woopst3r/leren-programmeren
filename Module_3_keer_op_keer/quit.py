count = 0

while True:  
    vraag = input("Waar kijk je naar?")
    if vraag != "quit":
        count = count + 1
    else:
        print (f"It took you {count} tries before you typed quit.")
        quit()

