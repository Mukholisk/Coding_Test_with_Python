N, M, K = map(int, input().split())
ary = list(map(int, input().split()))

ary.sort()
first = ary[-1]
second = ary[-2]
output = 0

while True:
    for i in range(K):
        if M == 0:
            break
        output += first
        M -= 1
    if M == 0:
        break
    output += second
    M -= 1

print(output)