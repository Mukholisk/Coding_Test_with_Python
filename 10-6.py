# 위상 정렬(Topology Sort): 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용.
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
# 예시) 선수과목을 고려한 학습 순서 설정-> 진입차수가 낮은 노드부터 처리

from collections import deque

v, e = map(int, input().split())
indegree = [0 for _ in range(v+1)]
graph = [[] for _ in range(v+1)]

for _ in range(e):
    s, e = map(int, input().split())
    graph[s].append(e)
    indegree[e] += 1

def topology_sort():
    answer = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        cur = q.popleft() # 진입차수가 0인 노드를 꺼내서
        answer.append(cur) # 저장

        for next_ in graph[cur]:
            indegree[next_] -= 1

            if indegree[next_] == 0:
                q.append(next_)

    for node in answer:
        print(node, end=' ')

topology_sort()

'''
input
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

output
1 2 5 3 6 4 7
'''