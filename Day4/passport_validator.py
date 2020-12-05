import pandas as pd

with open("Day4/data.txt", "r") as data:
    lines = data.readlines()

stringInput = "".join(lines)
data = stringInput.split("\n\n")

validCount = 0
count = 0
# Loop through every item in dataframe
for i in data:

    # Replace any "\n"s with whitespace so we can count the no. fields
    newInput = i.replace("\n", " ")

    # If there are 8 fields it must be valid
    fields = newInput.split(" ")
    fields.sort()

    if (count < 10):
        print("Count:", count, newInput)
        print("Fields:", fields)
        print(" ")
        count +=1
    
    if(len(fields) >= 8):
        validCount += 1
    
    # If there are 7 fields we need to check if the optional "cid" field is present to determine validity
    if (len(fields) == 7):
        if (not "cid" in newInput):
            validCount += 1

print("Number of valid passports:", validCount)