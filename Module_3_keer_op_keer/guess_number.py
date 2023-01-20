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

while rounds < max_rounds:
    #generates a random number between 1-1000
    antword = random.randint(1,1000)
    #increases the round by 1
    rounds += 1
    #resets the number of consecutive fails for each new round
    achterelkaar_fails = 0

    #prompts the user to input a number between 1-1000

    while achterelkaar_fails < max_achterelkaar_fails:
        try:
            print(antword)
            guess = int(input("Geef een getal tussen 1-1000: "))

            #checks if the guessed number is correct
            if guess == antword:
                print ("Correct je hebt het juist antword geraden!")
                score += 1
                break
            else:
                achterelkaar_fails += 1
                if achterelkaar_fails == max_achterelkaar_fails:
                    print ("Je hebt 10 keer acheter elkaar het verkeerde antword geraden. Het juiste antword was", antword)
                else:
                    if abs (antword-guess) <=20:
                        print("Heel Warm!")
                    elif abs (antword-guess) <=50:
                        print("Warm!")
                    if guess < antword:
                        print("Hoger")
                    elif guess > antword:
                        print("Lager")
            #prints the current score
            print("Je huidige score is:", score)
        except:
            print("Type in a valid number.")

    if round == max_rounds:
        print("Je hebt alle rondes gebruikt: ", rounds, "Het juiste antword was: ", antword)
    else:
        print("Nog", max_rounds - rounds, "rondes over")

    print("Je totale score is: ", score, "van de maximaal", max_score)