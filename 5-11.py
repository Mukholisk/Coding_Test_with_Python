from collections import deque

# U, D, L, R
dx = [-1, +1, +0, +0]
dy = [+0, +0, -1, +1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def BFS(graph, x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        cur = queue.popleft()
        cx, cy = cur[0], cur[1]

        if cx == len(graph) and cy == len(graph[0]):
            break

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if in_range(nx, ny) and graph[nx][ny] == 1:
                graph[nx][ny] = graph[cx][cy] + 1
                queue.append((nx, ny))

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

BFS(graph, 0, 0)

print(graph[N-1][M-1])
