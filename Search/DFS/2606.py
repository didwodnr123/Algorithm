from collections import deque

def bfs():
    queue = deque()
    queue.append(1)
    bfs_visited[1] = True
    while queue:
        q = queue.popleft()
        for i in range(n+1):
            if not bfs_visited[i] and graph[q][i] == 1:
                bfs_visited[i] = True
                queue.append(i)

def dfs(v):
    dfs_visited[v] = True
    for i in range(n+1):
        if not dfs_visited[i] and graph[v][i] == 1:
            dfs(i)
    

n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
bfs_visited = [False] * (n+1)
dfs_visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
bfs()
print(sum(bfs_visited) - 1)
dfs(1)
print(sum(dfs_visited) - 1)