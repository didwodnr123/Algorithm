N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))
apt = []
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    matrix[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # out of map
        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
            continue
        # wall
        if matrix[nx][ny] == 0:
            continue
        if matrix[nx][ny] == 1:
            dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            cnt = 0
            dfs(i, j)
            apt.append(cnt)

print(len(apt))
apt.sort()
for i in apt:
    print(i)