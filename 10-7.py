# 팀 결성: 서로소 집합 알고리즘
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
team = [i for i in range(N+1)]
answer = []
for _ in range(M):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        union_parent(team, a, b)
    else:
        if find_parent(team, a) == find_parent(team, b):
            answer.append("YES")
        else:
            answer.append("NO")

for a in answer:
    print(a)

'''
input
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

output
NO
NO
YES
'''
