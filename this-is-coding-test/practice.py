"""
4 5
00110
00011
11111
00000
"""
n, m = map(int, input().split())
graph = []

# 입력 받아서 graph 채우기
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x: int, y: int) -> bool:
    if x < 0 or x > n - 1 or y < 0 or y > m - 1:
        return False

    elif graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
