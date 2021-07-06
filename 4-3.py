data = input()

row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

output = 0
for s in steps:
    next_row = row + s[0]
    next_column = column + s[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        output += 1

print(output)