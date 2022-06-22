import sys, heapq
input = sys.stdin.readline
INF = 9999999999

N, M, C = map(int, input().split())
graph = [[] for _ in range(N)]
dist = [INF] * N

for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x-1].append((z, y-1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        sw, se = heapq.heappop(q)

        # start 기존 최단거리가 입력된 거리보다 짧은 경우(이미 처리가 되어 고려할 필요가 없는 경우)
        if dist[se] < sw:
            continue
            
        for next_ in graph[se]:
            nw, ne = next_
            cost = dist[se] + nw # 현재까지의 최단 거리 + 다음 노드까지의 거리(A)
            if cost < dist[ne]: # A가 다음까지의 최단 거리보다 짧은 경우 갱신
                dist[ne] = cost
                heapq.heappush(q, (cost, ne))

dijkstra(C-1)

count = 0
for i in range(N):
    if dist[i] == INF or i == C-1:
        dist[i] = -1
        continue
    count += 1

max_time = max(dist)

print(count, max_time)
