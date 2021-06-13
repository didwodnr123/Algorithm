from collections import deque

def bfs(x, y):
    # queue 생성
    queue = deque()
    # 큐에 첫 시작 지점 넣기
    queue.append((x, y))
    while queue: # 큐가 비어있지 않다면
        x, y = queue.popleft() # 큐에서 pop
        for i in range(4): # 상 하 좌 우, 이동할 수 있는 지점 체크 
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖으로 나간다면 무시
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue
            # 벽이라면 무시
            if graph[nx][ny] == 0:
                continue
            # 이동할 수 있고, 처음 방문한다면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 다음 위치 = 그래프 전 위치 +1
                queue.append((nx, ny)) # 큐에 다음 위치 삽입
    # 마지막 그래프 좌표의 값 == 이동횟수 출력
    return graph[N-1][M-1]

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))