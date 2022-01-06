import sys 
sys.setrecursionlimit(10000)

def dfs(x, y):
    matrix[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>N-1 or ny>M-1:
            continue
        if matrix[nx][ny] == 0:
            continue
        if matrix[nx][ny] == 1:
            dfs(nx, ny)

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        matrix[b][a] = 1
    
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)