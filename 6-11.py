N = int(input())
student = []

for _ in range(N):
    name, score = input().split()
    student.append((name, int(score)))

student.sort(key = lambda s: s[1])

for s in student:
    print(s[0], end=' ')
