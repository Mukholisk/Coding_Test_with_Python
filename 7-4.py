import sys

input = sys.stdin.readline

lst = []
for _ in range(3):
    # lst.append(list(map(int, input().split())))
    # lst.append(list(input())) # str: [['m', 'u', 'k', 'h', 'o', '\n'], ['m', 'u', 'k', ' ', 'h', 'o', '\n'], ['z', 'z', '\n']]
    lst.append(list(input().rstrip())) # str: [['m', 'u', 'k', 'h', 'o'], ['m', 'u', 'k', ' ', 'h', 'o'], ['z', 'z']]

print(lst)
