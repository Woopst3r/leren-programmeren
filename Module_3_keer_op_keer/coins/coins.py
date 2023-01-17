# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))) # Hij vraagt hier hoeveel hij moet betalen.
paid = int(float(input('Paid amount: '))) # Hoeveel geld hij gegeven heeft.
change = paid - toPay # Hoeveel hij terug moet terug geven.

if change > 0: # Als hij wat terug moet geven boven de 0 is voert hij de code hieronder uit.
  coinValue = 5 # Hier begint hij coinValue met 5 euro.
  returnTicket = ''
  
  while change > 0 and coinValue > 0: # Hij voert een while loop uit als wat hij terug moet geven boven 0 is en coinValue boven 0.
    nrCoins = change // coinValue # Hier berekent hij hoeveel munten hij maximaal mag terug geven.

    if nrCoins > 0: # Als het aantal munten hoger dan 0 is voert hij de code hieronder uit.
      print('return maximal', nrCoins, 'coins of', coinValue, 'euro!' ) # Hier print hij het maximaal aantal munten van bijvoorbeeld 50 cent dat je kan terug geven.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' euro did you return? ')) # Hier vraagt hij hoeveel munten van een soort dat je terug hebt gegeven.
      change -= nrCoinsReturned * coinValue # Hier berekent hij hoeveel je nog moet terug geven.

      returnTicket += str(nrCoinsReturned)
      returnTicket += 'x '
      returnTicket += str(coinValue)
      returnTicket += ' euro munt teruggegven\n'

# comment on code below: Als de coinValue bijvoorbeeld 5 is dan wordt hij 2 nadat je de vraag beantwoord.
    if coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    elif coinValue == 1:
      coinValue = 0.50 
    elif coinValue == 0.50:
      coinValue = 0.20
    elif coinValue == 0.20:
      coinValue = 0.10
    elif coinValue == 0.10:
      coinValue = 0.05
    elif coinValue == 0.05:
      coinValue = 0.02
    elif coinValue == 0.02:
      coinValue = 0.01
    else:
      coinValue = 0
elif change <= 0:
  print("Je hebt niet genoeg gegeven. Probeer opnieuw!")


if change > 0: # Als je nog niet alles terug hebt gegeven print hij de code eronder van hoeveel hij niet terug gaf. Als je wel alles terug gaf print hij welke munten je terug gaf.
  print('Change not returned: ', str(change) + ' euro')
elif change == 0:
  print(returnTicket)