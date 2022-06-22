# 다익스트라
import heapq
import sys

input = sys.stdin.readline
INF = 99999999999

N, M = map(int, input().split())
start = int(input())

graph = [[] for i in range(N)]
dist = [INF] * N
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        w, e = heapq.heappop(q)

        if dist[e] < w: # 처리할 필요가 없음
            continue
            
        for nextnode in graph[e]:
            nw, ne = nextnode
            cost = w + nw

            if cost < dist[ne]:
                dist[ne] = cost
                heapq.heappush(q, (cost, ne))

dijkstra(start)

for i in range(N):
    print(dist[i] if dist[i] != INF else 'INF')
