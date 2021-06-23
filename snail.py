def snail(N):
    global cnt
    global x, y

    while N > 0:
        N -= 1
        for _ in range(N):
            x += dx[0]
            y += dy[0]
            if lst[x][y] != 0:
                x -= dx[0]
                y -= dy[0]
                break
            cnt += 1
            lst[x][y] = cnt
        for _ in range(N):
            x += dx[1]
            y += dy[1]
            if lst[x][y] != 0:
                x -= dx[1]
                y -= dy[1]
                break
            cnt += 1
            lst[x][y] = cnt
        N -= 1
        for _ in range(N):
            x += dx[2]
            y += dy[2]
            if lst[x][y] != 0:
                x -= dx[2]
                y -= dy[2]
                break
            cnt += 1
            lst[x][y] = cnt

N = int(input())

lst = [[0] * N for _ in range(N)]
# 아래대각, 위, 오른쪽
dx = [1, -1, 0]
dy = [-1, 0, 1]

x = 0
y = N-1
cnt = 1
lst[x][y] = cnt
snail(N)
print(lst)