# BFS
from collections import deque

def BFS(graph, visited, s):
    queue = deque()

    queue.append(s)
    visited[s] = 1

    while queue:
        e = queue.popleft()
        print(e, end=' ')

        for i in graph[e]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

graph = [
    [1, 2, 7],
    [0, 6],
    [0, 3, 4],
    [2, 4],
    [2, 3],
    [6],
    [1, 5, 7],
    [0, 6]
]

visited = [0] * 8
BFS(graph, visited, 0)