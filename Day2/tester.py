import pandas as pd

data = pd.read_csv("Day2/passwords.txt", sep=":", header=None)

print("cond:", data[0][0], "   pass:", data[1][0])

validCount = 0

password = data[1][0].replace(" ", "")
conditions = data[0][0].split(" ")
finalConditions = (conditions[0].split("-"), conditions[1])

print("Letter we check:", password[int(finalConditions[0][0])-1], "Letter we're looking for:", conditions[1])
print("Index we check:", int(finalConditions[0][0])-1)
lowIndex = int(finalConditions[0][0])-1
highIndex = int(finalConditions[0][1])-1

print(password[1])
if (password[lowIndex] == conditions[1] and password[highIndex] != conditions[1]):
    validCount += 1
elif (password[lowIndex] != conditions[1] and password[highIndex] == conditions[1]):
    validCount += 1

print("Valid passwords:", validCount)