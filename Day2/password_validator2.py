import pandas as pd

data = pd.read_csv("Day2/passwords.txt", sep=":", header=None)

print(data)

validCount = 0
for i in range(len(data[1])):
    password = data[1][i].replace(" ", "")
    conditions = data[0][i].split(" ")
    finalConditions = (conditions[0].split("-"), conditions[1])
    lowIndex = int(finalConditions[0][0])-1
    highIndex = int(finalConditions[0][1])-1

    if (password[lowIndex] == conditions[1] and password[highIndex] != conditions[1]):
        validCount += 1
    elif (password[lowIndex] != conditions[1] and password[highIndex] == conditions[1]):
        validCount += 1 

print(validCount)