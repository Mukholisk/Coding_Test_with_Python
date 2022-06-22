# 플로이드 워셜
import sys

input = sys.stdin.readline
INF = 99999999999

N = int(input())
M = int(input())

graph = [
    [INF for _ in range(N)]
    for i in range(N)
]
for i in range(N):
    for j in range(i, i+1):
        graph[i][j] = 0

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s-1][e-1] = w

# 알고리즘
for m in range(N):
    for s in range(N):
        for e in range(N):
            if graph[s][e] > graph[s][m] + graph[m][e]:
                graph[s][e] = graph[s][m] + graph[m][e]

for i in range(N):
    for j in range(N):
        print(graph[i][j] if graph[i][j] != INF else "INF", end = ' ')
    print()
