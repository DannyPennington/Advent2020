import pandas as pd

data = pd.read_csv("Day2/passwords.txt", sep=":", header=None)

print(data)

validCount = 0
for i in range(len(data[1])):
    password = data[1][i]
    conditions = data[0][i].split(" ")
    finalConditions = (conditions[0].split("-"), conditions[1])
    count = 0
    for i in password:
        if i == finalConditions[1]:
            count +=1
    if (int(finalConditions[0][0]) <= count <= int(finalConditions[0][1])):
        validCount +=1

print(validCount)