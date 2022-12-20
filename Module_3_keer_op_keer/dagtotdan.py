dagen = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]

while True:
    dag = input ("Welke dag is het?: ")
    if dag in dagen:
        break
num = 0
restdagen = True
while restdagen:
    print(dagen[num])
    if dag == dagen [num]:
        break
    num = num + 1