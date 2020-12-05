import pandas as pd

data = pd.read_csv("expenses.txt", sep=" ", header=None)


for i in data[0]:
    for j in data[0]:
        for k in data[0]:
            total = i + j + k

            if total == 2020:
                numbers = (i, j, k)
                break

print(numbers)
print(numbers[0]*numbers[1]*numbers[2])