import pandas as pd

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

# We already know what bags our bag can hold, so we need to loop through the sublevels of each of those bags, storing the number of bags each time

x = False
while x:
    # Loop through our bag's sub-bags
    bags = conditionDict["shiny gold"]

bags = conditionDict["shiny gold"]
print(bags)