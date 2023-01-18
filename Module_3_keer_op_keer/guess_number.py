import random

#variable score
score = 0
max_score = 20

#variable rounds
rounds = 0
max_rounds = 20

#fails in a row
achterelkaar_fails = 0
max_achterelkaar_fails = 10

#genereert een nummer tussen 1-1000
antword = random.randint(1,1000)

#vraag je om een getal te geven tussen 1-1000.
while rounds < max_rounds:  
    try:
        guess = int(input("Geef een getal tussen 1-1000: "))
        
        #verhoogt ronde met 1
        rounds += 1

        #coontroleren of het graden getal correct is
        
        if guess == antword:
            print ("Correct je hebt het juist antword geraden!")
            score += 2
            achterelkaar_fails = 0
            break
        else:
            achterelkaar_fails += 1
            if achterelkaar_fails == max_achterelkaar_fails:
                print ("Je hebt 10 keer acheter elkaar het verkeerde antword geraden. Het juste antword was", antword)
                break
            else:
                if abs (antword-guess) <=50:
                    print("Warm!")
                if abs (antword-guess) <=20:
                    print("Heel Warm!")
                if guess < antword:
                    print("Hoger")
                elif guess > antword:
                    print("Lager")
        #print huidige score
        print("Je huidige score is:", score)
        if round == max_rounds:
            print("J hebt alle rondes gebruik: ", rounds, "Het juiste antword was: ", antword)
        else:
            print("nog:", max_rounds - rounds, "rondes over")
    except:
        print("Type in a falid number.")