def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]: # True가 아니면
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현
# 1>2, 2>7, 7>6 7>8순서로 갔다가 1>3 3>4 4>5
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
dfs(graph, 1, visited)

# dfs는 스택 방식(재귀 함수), bfs는 큐 방식(deque 라이브러리) 이용
