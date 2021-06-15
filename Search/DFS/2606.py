N = int(input())
n_edge = int(input())

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(n_edge):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    visited[v] = True
    for i in range(1, N+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

dfs(1)
print(visited.count(True) - 1)