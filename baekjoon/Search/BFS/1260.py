from collections import deque

def dfs(v):
    visited_1[v] = True
    print(v, end=' ')
    for i in range(1, N+1):
        if not visited_1[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited_2[v] = True
    while queue:
        v = queue.popleft() 
        print(v, end=' ')
        for i in range(1, N+1):
            if not visited_2[i] and graph[v][i] == 1:
                visited_2[i] = True
                queue.append(i)

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited_1 = [False] * (N+1)
visited_2 = [False] * (N+1)

for _ in range(1, M+1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(V)
print()
bfs(V)







































