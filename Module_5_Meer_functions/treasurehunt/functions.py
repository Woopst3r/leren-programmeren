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
    return getFromListByKeyIs(people, 'advanturing' , True)

def getShareWithFriends(friends:list) -> int:
    return getShareWithFriends(friends, 'shareWith' , True)

def getAdventuringFriends(friends:list) -> list:
    return getAdventuringFriends(friends, 'advanturing' , True)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    return (silver2gold(horses * COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS) + ((tents * COST_TENT_GOLD_PER_WEEK) * 2) 

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
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

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