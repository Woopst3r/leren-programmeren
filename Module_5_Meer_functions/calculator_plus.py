def division(n1, n2):
    return n1 / n2
def addition(n1, n2):
    return n1 + n2
def subtraction(n1, n2):
    return n1 - n2
def multiplication(n1, n2):
    return n1 * n2

round_one = True
nr1 = False
nr2 = False

while True:
    if round_one == True:
        choice = input("wat wilt u doen?\n A) getallen optellen\n B) getallen aftrekken\n C) getallen vermenigvuldigen\n D) getallen delen\n E) getal ophogen\n F) getal verlagen\n G) getal verdubbelen\n H) getal halveren\n").lower()
    else:
        choice = input(f"Wil je wat met de uitkomst {antwoord} doen?\n A) iets optellen\n B) iets aftrekken\n C) met iets vermenigvuldigen\n D) ergens door delen\n E) ophogen\n F) verlagen\n G) verdubbelen\n H) halveren\n I) niets\n").lower()
        n1 = antwoord
        nr2 = False
    
    if choice in ("a","b","c","d","c","d","e","f","g","h","i"):
        round_one = False
    
    if choice in ("a", "b", "c", "d", "e", "f", "g", "h"):
        firstRound = False
        if nr1 == False:
            n1 = float(input("Welk getal? \n"))
        if choice in ("a", "b"):
            if nr2 == False:
                n2 = float(input(f"Welk getal? \n"))
        if choice in ("c", "d"):
            if nr2 == False:
                while True:
                    n2 = float(input(f"Welk getal? \n"))
                    if n2 == 0:
                        print("Kan niet delen met 0. \n")
                    else:
                        break
        if choice in ("e", "f"):
            n2 = 1
        if choice in ("g", "h"):
            n2 = 2
        nr1, nr2 = True, True
    if choice == "a"or choice=="e":
        antwoord = addition(n1, n2)
        print(f"{n1} + {n2} = {antwoord}")
    elif choice == "b":
        antwoord = subtraction(n1, n2)
        print(f"{n1} - {n2} = {antwoord}")
    elif choice == "c":
        antwoord = multiplication(n1, n2)
        print(f"{n1} x {n2} = {antwoord}")
    elif choice == "d":
        antwoord = division(n1, n2)
        print(f"{n1} : {n2} = {antwoord}")
    elif choice == "f":
        antwoord = subtraction(n1, n2) 
        print(f"{n1} - {n2} = {antwoord}")
    elif choice == "g":
        antwoord = multiplication(n1, n2) 
        print(f"{n1} x {n2} = {antwoord}")
    elif choice == "h":
        antwoord = division(n1, n2) 
        print(f"{n1} : {n2} = {antwoord}")
    elif choice == "i" and firstRound == False:
        print("Einde berekening. \n")
        break
    else:
        print("Dat is geen geldig antwoord! \n")
    
    print("-------------------------")