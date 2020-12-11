with open("Day6/data.txt", "r") as data:
    lines = data.readlines()

stringInput = "".join(lines)
data = stringInput.split("\n\n")
yesTotal = 0

for group in data:
    groupSet = set()
    # Split groups up based on new lines
    peopleList = group.split("\n")

    if (len(peopleList) == 1):
        # Only one person so all their answers go in 
        for letter in peopleList[0]:
            groupSet.add(letter)
    else:
        personIndex = 0
        for person in peopleList:
            tempSet = set()
            # Add all that users yes' to a set
            for letter in person:
                tempSet.add(letter)
            # If this is our first run through set that as the overall set, otherwise take the intersection of the sets analysed so far and the new set
            if (personIndex > 0):
                groupSet = groupSet.intersection(tempSet)
            else:
                groupSet = tempSet
            personIndex +=1

    yesTotal += len(groupSet)

print(yesTotal)