def ask_name_and_age():
    name = input("Voer de naam in: ")
    age = int(input("Voer de leeftijd in: "))
    return {"name": name, "age": age}

names_and_ages = []
Herhaal = True

while Herhaal:
    names_and_ages.append(ask_name_and_age())
    user_input = input("Toets enter om door te gaan of stop om te printen: ")
    if user_input.lower() == "stop":
        Herhaal=False


print("Namen en leeftijden:")
for name_and_age in names_and_ages:
    print(name_and_age["name"] + " is " + str(name_and_age["age"]) + " jaar oud.")