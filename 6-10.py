N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))

lst.sort(reverse=True)
for n in lst:
    print(n, end=' ')
