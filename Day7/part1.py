import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

data = pd.read_csv("Day7/data.txt", sep="\n", header=None)

conditionDict = {}

for condition in data[0]:
    # Seperate colour of bag from what it holds
    splitRow = condition.split("bags contain")
    colour = splitRow[0].strip()
    # 3 options: no other type of bag, 1 other type of bag, multiple other types of bag
    contains = []
    if "no other bags" in splitRow[1]:
        # If a bag holds no other bags it is useless to us in this question so we do nothing
        pass
    elif "," in splitRow[1]:
        temp = splitRow[1].split(",")
        for i in temp:
            values = i.strip().split(" ")
            contains.append((values[0], values[1] + " " + values[2]))
    else:
        values = splitRow[1].strip().split(" ")
        contains.append((values[0], values[1] + " " + values[2]))

    conditionDict.update({colour: contains})

# Now we have a dictionary with every bag colour and a list of bags it can hold

def bagHolderFinder(myDict, colour):
    # Find every bag that can directly hold the colour requsted. Return as list of strings
    bags = []
    for key, value in myDict.items():
        for cond in value:
            if cond[1] == colour:
                bags.append(key)
                break
    return bags

def subBagFinder(myDict, bags):
    # Takes a flat list of bags and finds each bag that can hold any of those input bags. Returns a list of strings
    subBags = []
    for bag in bags:
        subBags.append(bagHolderFinder(conditionDict, bag))
    flatSubBags = [y for x in subBags for y in x]
    return flatSubBags

def ultimateBagCombinator(myDict, colour):
    allBags = set()
    bagList = bagHolderFinder(myDict, colour)

    for bag in bagList:
        allBags.add(bag)

    x = True
    loopCount = 1

    # Then we will do a while loop that will break when we reach the highest tier of bag (bags no other bag can hold)
    while x:
        bagList = subBagFinder(myDict, bagList)
        # If our sub-bag list is empty we have reached the pinnacle of bags
        if len(bagList) == 0:
            break

        for bag in bagList:
            allBags.add(bag)
        loopCount += 1

    totalBags = len(allBags)
    return totalBags


def plotData(loopCount, bagsList):
    fig, ax = plt.subplots()
    ax.plot(range(loopCount), bagsList, color="r")

    ax.set_ylim(0,50)
    ax.set_xlim(0, 10)
    ax.set_xlabel("Loop count")
    ax.set_ylabel("No. bags")

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    plt.show()


x = ultimateBagCombinator(conditionDict, "shiny gold")

print(x)
