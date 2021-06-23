def dfs(x, y):
    field[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>h-1 or ny>w-1:
            continue
        if field[nx][ny] == 0:
            continue
        if field[nx][ny] == 1:
            dfs(nx, ny)

answer = []

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    field = []
    for j in range(h):
        field.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                dfs(i, j)
                cnt += 1

    answer.append(cnt)

for ans in answer:
    print(ans)