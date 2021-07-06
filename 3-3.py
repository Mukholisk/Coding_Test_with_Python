N, M = map(int, input().split())
output = 0
for i in range(N):
    ary = map(int, input().split())
    output = max(min(ary), output)
print(output)