# 크루스칼(https://www.acmicpc.net/problem/1647) 도시 분할 계획, 백준 G4
# 최소 비용으로 2구간을 만들기: 최소신장트리를 찾은 후, 가장 큰 가중치를 가지는 edge를 없애면 된다.
import sys
input = sys.stdin.readline # 알고리즘이 "맞는데 왜 틀림?" -> input 대신 sys.stdin.readline을 쓰자.

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
city = [i for i in range(N+1)]

# >크루스칼
edges = []
answer = 0

for _ in range(M):
    start, end, weight = map(int, input().split())
    edges.append((weight, start, end))

edges.sort()
# >크루스칼

max_edge = -1 # 최소 비용으로 2구간을 만들기: 최소신장트리를 찾은 후, 가장 큰 가중치를 가지는 edge를 없애면 된다.
for w, s, e in edges:
    w, s, e = edge

    # >서로소
    if find_parent(city, s) != find_parent(city, e):
        union_parent(city, s, e)
        answer += w
        max_edge = w
    # >서로소

print(answer - max_edge)
