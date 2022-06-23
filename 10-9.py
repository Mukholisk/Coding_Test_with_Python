from collections import deque

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

N = int(input())
indegree = [0] * (N+1) # 선수과목-위상정렬
graph = [[] for _ in range(N+1)] # 해당 과목의 선수과목
time = [0] * (N+1) # 과목별 이수 시간

for i in range(1, N+1):
    in_ = list(map(int, input().split()))
    time[i] = in_[0]
    for d in in_[1:-1]:
        indegree[i] += 1
        graph[d].append(i)

def topology_sort():
    answer = time[:]
    q = deque()

    # 초기값: 진입차수가 0인 노드
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()

        for next_ in graph[cur]:
            answer[next_] = max(answer[next_], answer[cur] + time[next_])
            indegree[next_] -= 1

            if indegree[next_] == 0:
                q.append(next_)

    for i in range(1, N+1):
        print(answer[i])

topology_sort()

'''
input
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

output
10
20
14
18
17
'''
