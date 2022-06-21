n, target = input().split()
n = int(n)
lst = list(input().split())

for i in range(n):
    if lst[i] == target:
        print(i+1)
        break
