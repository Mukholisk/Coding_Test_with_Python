# 서로소 집합을 통한 사이클 판별 알고리즘
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

# 노드 개수, 간선 개수
v, e = map(int, input().split())
parent = [i for i in range(v+1)]

is_cycle = False

for i in range(e):
    a, b = map(int, input().split())

    if find_parent(parent, a) == find_parent(parent, b):
        is_cycle = True
        break
    union_parent(parent, a, b)

print(is_cycle)
for i in range(1, v+1):
    print(parent[i],end=' ')
