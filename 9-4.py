import heapq
INF = 9999999999

N, M = map(int, input().split())

# 다익스트라
dist = [INF for _ in range(N)]
graph = [[] for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s-1].append((1, e-1))
    graph[e-1].append((1, s-1))

X, K = map(int, input().split())
X -= 1
K -= 1

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        sw, se = heapq.heappop(q)

        if dist[se] < sw:
            continue
        for nextnode in graph[se]:
            nw, ne = nextnode
            cost = dist[se] + 1
            if cost < dist[ne]:
                dist[ne] = cost
                heapq.heappush(q, (cost, ne))
    
    return dist[end]

answer = dijkstra(0, K) + dijkstra(K, X)

# 플로이드 워셜
'''
graph = [
    [INF for _ in range(N)]
    for _ in range(N)
]
for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    s, e = map(int, input().split())
    graph[s-1][e-1] = 1
    graph[e-1][s-1] = 1

X, K = map(int, input().split())
X -= 1
K -= 1

for m in range(N):
    for s in range(N):
        for e in range(N):
            if graph[s][e] > graph[s][m] + graph[m][e]:
                graph[s][e] = graph[s][m] + graph[m][e]

answer = graph[0][K] + graph[K][X]
'''

print(answer if answer < INF else -1)
