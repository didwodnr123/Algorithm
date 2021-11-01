from collections import deque

def bfs(i, j):
    queue = deque()
    queue.append((i,j))
    board[i][j] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>n-1 or ny>n-1:
                continue
            elif board[nx][ny] == 1:
                queue.append((nx,ny))
                board[nx][ny] = 0
                cnt += 1
                
    return cnt
        

lst = []
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
for _ in range(n):
    board.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            lst.append(bfs(i,j))
            
print(len(lst))
for i in sorted(lst):
    print(i)
