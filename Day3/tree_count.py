import pandas as pd

data = pd.read_csv("Day3/data.txt", sep=" ", header=None)

print(data)
# Each row has a length of 31 so we probs need to modulus to mock the loop

def calculateCollisions(right, down):
    xPos = 0
    yPos = 0
    treeCount = 0

    # Loop through each row in the dataframe
    for i in data[0]:
        # Make sure we don't overshoot the bottom of the slope
        if (yPos < len(data[0])):
            # Check if we are on a tree
            if ((data[0][yPos])[xPos] == "#"):
                treeCount += 1
            # Increment position based on input parameters
            xPos += int(right)
            yPos += int(down)
            # Account for x looping every 31 x positions
            xPos = xPos % 31

    print(f"Tree count for {right} across and {down} down is:", treeCount)
    return treeCount

treeTotal = calculateCollisions(1,1) * calculateCollisions(3,1) * calculateCollisions(5,1) * calculateCollisions(7,1) * calculateCollisions(1,2)
print(f"Multiplication of the 5 slopes is: {treeTotal}")