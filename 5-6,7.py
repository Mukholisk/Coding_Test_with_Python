INF = 99999999

# 인접 행렬
graph1 = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

# 인접 리스트
graph = [[] for _ in range(3)]

# 도착노드, 거리
graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
graph[2].append((0, 5))
