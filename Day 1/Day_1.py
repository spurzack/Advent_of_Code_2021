import pandas as pd

# Part 1

data = pd.read_csv('Puzzle_Input', sep=" ", header=None)

total_1 = 0
for row in range(len(data)-1):
    if data[0][row] < data[0][row+1]:
        total_1 = total_1 + 1

print(total_1)

# Part 2

total_2 = 0
for row in range(len(data)-3):
    if (data[0][row] + data[0][row+1] + data[0][row+2]) < (data[0][row+1] + data[0][row+2] + data[0][row+3]):
        total_2 = total_2 + 1

print(total_2)