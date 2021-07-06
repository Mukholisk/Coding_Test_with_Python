N = int(input())
cmd = input().split()

x = 1
y = 1

for c in cmd:
    if c == "L":
        if y > 1:
            y -= 1
    elif c == "R":
        if y < N:
            y += 1
    elif c == "U":
        if x > 1:
            x -= 1
    elif c == "D":
        if x < N:
            x += 1

print(x, y)