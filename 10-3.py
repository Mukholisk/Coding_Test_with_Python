# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드까지 재귀적으로 찾기
    if parent[x] != x: # 최상위 노드가 아님
        parent[x] = find_parent(parent, parent[x]) # 경로 압축 기법 소스코드: 부모 테이블 값을 바로 갱신(해당 노드의 루트 노드가 바로 부모 노드가 됨) -> 해당 노드의 부모 노드는 바로 최상의 노드가 됨.

    # return x
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블

# 일단 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# Union 연산
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()

# 각 원소의 부모 노드 출력
for i in range(1, v+1):
    print("%d: %d" % (i, parent[i]))

'''
1-4 // 1 2 3 1 5 6
2-3 // 1 2 2 1 5 6
2-4 // 1 1 1 1 5 6
5-6 // 1 1 1 1 5 5
'''
