def in_range(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8

data = input()

row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

output = 0
for s in steps:
    nr = row + s[0]
    nc = column + s[1]

    if in_range(nr, nc):
        output += 1

print(output)