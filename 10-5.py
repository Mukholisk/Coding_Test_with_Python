'''
신장 트리(Spanning Tree): 하나의 그래프가 있을 때 모든 노드를 포함하면서 '사이클이 존재하지 않는' 부분 그래프
크루스칼 알고리즘(Kruskal Algorithm): 최소 비용 신장 트리를 찾는 알고리즘 == 모든 노드를 연결할 때 최소한의 비용으로 연결하는 알고리즘.
- 가중치가 낮은 순으로 정렬 후, 사이클이 생기지 않는 한에서 연결 -> 가장 적은 비용으로 모든 노드를 연결할 수 있음(그리디 알고리즘)
'''
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

v, e = map(int, input().split())
parent = [i for i in range(v+1)]

edges = []
total_weight = 0

for _ in range(e):
    start, end, weight = map(int, input().split())
    edges.append((weight, start, end))

edges.sort()

for edge in edges:
    weight, start, end = edge

    # 사이클이 형성되지 않는 경우에만 집합에 포함
    if find_parent(parent, start) != find_parent(parent, end):
        union_parent(parent, start, end)
        total_weight += weight

print(total_weight)

'''
input
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

output
159
'''
