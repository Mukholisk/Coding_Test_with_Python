def in_range(x, y):
    return 1 <= x <= N and 1 <= y <= N

# U, D, L, R
dx = [-1, +1, +0, +0]
dy = [+0, +0, -1, +1]
di = {'U':0, 'D':1, 'L':2, 'R':3}

N = int(input())
cmds = input().split()

x = 1
y = 1

for c in cmds:
    nx = x + dx[di[c]]
    ny = y + dy[di[c]]

    if in_range(nx, ny):
        x, y = nx, ny 

print(x, y)
