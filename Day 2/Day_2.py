import pandas as pd

# --- Day 2: Dive! ---
# Part 1 and 2

df = pd.read_csv('Day_2_Input', sep=" ", header=None)

x = 0
y = 0
a = 0
aDepth = 0

for row in range(len(df)):
    if df[0][row] == 'down':
        y = y + df[1][row]
        a = a + df[1][row]
    if df[0][row] == 'up':
        y = y - df[1][row]
        a = a - df[1][row]
    if df[0][row] == 'forward':
        x = x + df[1][row]
        aDepth = aDepth + (a * df[1][row])

print("Part 1 Final Position:", "x=", x, "y=", y)
print("Part 1 Answer:", x*y)

print("Part 2 Final Position:", "Aimed Depth=", aDepth, "x=", x, "y=", y)
print("Part 2 Answer:", x*aDepth)