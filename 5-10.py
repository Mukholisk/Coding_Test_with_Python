# U, D, L, R
dx = [-1, +1, +0, +0]
dy = [+0, +0, -1, +1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def DFS(graph, visited, cx, cy):
    visited[cx][cy] = 1

    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if in_range(nx, ny) and visited[nx][ny] == 0 and graph[nx][ny] == 0:
            DFS(graph, visited, nx, ny)

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

visited = [
    [0 for _ in range(M)]
    for _ in range(N)
]

count = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and graph[i][j] == 0:
            DFS(graph, visited, i, j)
            count += 1

print(count)
