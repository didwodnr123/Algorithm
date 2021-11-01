import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    lst[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx<0 or ny<0 or nx>h-1 or ny>w-1:
            continue
        elif lst[nx][ny] == 1:
            dfs(nx, ny)

cnt_lst = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        for cnt in cnt_lst:
            print(cnt)
        break
    lst = []
    for _ in range(h):
        lst.append(list(map(int, input().split())))
    
    cnt = 0
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    for i in range(h):
        for j in range(w):
            if lst[i][j] == 1:
                dfs(i, j)
                cnt += 1
    
    cnt_lst.append(cnt)