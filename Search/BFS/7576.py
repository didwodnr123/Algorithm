from collections import deque

def bfs(pos_list):
    queue = deque()
    for pos in pos_list:
        queue.append(pos)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny<0 or nx>n-1 or ny>m-1:
                continue
            elif graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
        
            
m, n = map(int, input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    graph.append(list(map(int, input().split())))

pos_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            pos_list.append((i,j))
            
bfs(pos_list)
maxx = 0
for row in graph:
    if 0 in row:
        maxx = 0
        break
    for r in row:
        if r > maxx:
            maxx = r

print(maxx-1)