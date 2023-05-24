import time
from termcolor import colored
from data import *
import math

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return 25 * amount

def getPersonCashInGold(personCash:dict) -> float:
    return copper2gold(personCash["copper"]) + silver2gold(personCash["silver"]) + platinum2gold(personCash["platinum"]) + personCash["gold"]

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    return round((copper2gold(people * COST_FOOD_HUMAN_COPPER_PER_DAY) + copper2gold(horses * COST_FOOD_HORSE_COPPER_PER_DAY)) * JOURNEY_IN_DAYS, 2)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lst = []
    for element in list:
        if element[key] == value:
            lst.append(element)
    return lst

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring' , True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, 'shareWith' , True)

def getAdventuringFriends(friends:list) -> list:
    return getFromListByKeyIs(getShareWithFriends(friends), 'adventuring' , True)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    return (silver2gold(horses * COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS) + ((tents * COST_TENT_GOLD_PER_WEEK) * math.ceil(JOURNEY_IN_DAYS / 7)) 

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    lst = []
    for item in items:
        itemText = f"{item['amount']}{item['unit']} {item['name']}"
        lst.append(itemText)
    return ', '.join(lst)

def getItemsValueInGold(items:list) -> float:
    gold = 0
    for item in items:
        if item["price"]["type"] == "gold":
            gold += item["price"]["amount"] * item["amount"]
        elif item["price"]["type"] == "silver":
            gold += silver2gold (item["price"]["amount"] * item["amount"])
        elif item["price"]["type"] == "copper":
            gold += copper2gold (item["price"]["amount"] * item["amount"])
        elif item["price"]["type"] == "platinum":
            gold += platinum2gold (item["price"]["amount"] * item["amount"])        
    return gold


##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total_gold = 0
    for person in people:
        total_gold += copper2gold(person['cash']['copper'])
        total_gold += silver2gold(person["cash"]["silver"])
        total_gold += platinum2gold(person["cash"]["platinum"])  
        total_gold += person["cash"]["gold"]
    return total_gold


##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    invest_list = []
    for investor in investors:
        if investor["profitReturn"] <= 10:
            invest_list.append(investor)
    return invest_list

def getAdventuringInvestors(investors:list) -> list:
    adventuring_list = []
    for investor in getInterestingInvestors(investors):
        if investor["adventuring"]:
            adventuring_list.append(investor)
    return adventuring_list

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    adventuring_len = len(getAdventuringInvestors(investors))

    
    gear_cost = adventuring_len * getItemsValueInGold(gear)

    InvestorFood = getJourneyFoodCostsInGold (adventuring_len, adventuring_len)
    investorRent = getTotalRentalCost (adventuring_len, adventuring_len)

    total_cost = gear_cost + InvestorFood + investorRent
    return total_cost

    


##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    HumanInn = silver2gold(people* COST_INN_HUMAN_SILVER_PER_NIGHT)
    HorsesInn = copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT)

    return math.floor(leftoverGold/(HumanInn + HorsesInn))

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    HumanInn = silver2gold(people* COST_INN_HUMAN_SILVER_PER_NIGHT)
    HorsesInn = copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT)

    return round(nightsInInn *(HumanInn + HorsesInn),2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    lst = []
    for investor in getInterestingInvestors(investors):
        lst.append(round(investor['profitReturn']/100 * profitGold,2))
    return lst

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    for gold in investorsCuts:
        profitGold -= gold
    return (round(profitGold / fellowship,2))

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    
    adventuringFriends = getAdventuringFriends(friends)
    
    adventuringInvestors = getAdventuringInvestors(investors)
    interestingInvestors = getInterestingInvestors(investors)
    
    investorsCuts = getInvestorsCuts(profitGold, investors)
    adventurercut = getAdventurerCut(profitGold, investorsCuts, len (adventuringFriends + adventuringInvestors)+1) 
    goldCut = profitGold - sum(investorsCuts)
    endGold = 0
    
    for person in people: 
        startGold = getCashInGoldFromPeople([person]) # Berekent hoeveel goud ze bijzig hebben.

        if person in interestingInvestors and person in adventuringInvestors: # Hoeveel goud een investeerder krijg die geïnteresseerd is en mee gaat op avontuur
            endGold = startGold + investorsCuts[investors.index(person)] + goldCut / len([mainCharacter] + adventuringFriends + adventuringInvestors)

        elif person in interestingInvestors: # Hoeveel goud geïnteresseerde investeerders krijgen
            endGold = startGold + investorsCuts[investors.index(person)]

        elif person in investors and person not in interestingInvestors: # Wat investeerders krijgen die niks mee te maken hebben
            endGold = startGold
        
        elif person in adventuringFriends: # Hoeveel goud vrienden krijgen die op avontuur gaan
            endGold = startGold + (goldCut / len([mainCharacter] + adventuringFriends + adventuringInvestors)) - 10 
            earnings[0]['end'] += 10

        elif person in friends and person not in adventuringFriends: # Hoeveel goud vrienden krijgen die je niet deelt
            endGold = startGold

        else: # Hoeveel de maincharacter krijgt
            endGold += startGold + adventurercut
        
        earnings.append({
        'name'   : person['name'],
        'start'  : startGold,
        'end'    : round(endGold, 2)
        })

    return earnings

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()