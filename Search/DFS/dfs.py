def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# index 0을 사용하지 않게 설정.
graph = [
    [],
    [2, 3, 8], # 1번 노드 인접 노드
    [1, 7], # 2번 노드 인접 노드
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)