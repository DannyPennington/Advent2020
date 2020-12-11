with open("Day6/data.txt", "r") as data:
    lines = data.readlines()

stringInput = "".join(lines)
data = stringInput.split("\n\n")
yesTotal = 0

for i in data:
    groupSet = set()
    # Remove any "\n" so we can only have the answers as one long string for the group
    newInput = i.replace("\n", "")

    # Go through each letter and add it to our set
    for i in newInput:
        groupSet.add(i)

    yesTotal += len(groupSet)

print(yesTotal)