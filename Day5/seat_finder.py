import pandas as pd

data = pd.read_csv("Day5/data.txt", sep=":", header=None)

# Each code is 10 digits with meaning spilt 7:3 so let's reformat dataframe
allIds = [*range(1, 806, 1)]
for i in data[0]:
    vertical = i[:7]
    horizontal = i[7:]

    # Now we have seperated the the values we can convert our number into binary format
    vertical = vertical.replace("F", "0").replace("B", "1")
    horizontal = horizontal.replace("L", "0").replace("R", "1")

    # Convert the binary into an Int
    row = int(vertical, 2)
    col = int(horizontal, 2)

    seatId = (row*8)+col
    if seatId in allIds:
        allIds.remove(seatId)


print(allIds)
