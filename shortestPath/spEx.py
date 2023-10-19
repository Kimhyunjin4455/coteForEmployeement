# 1번부터 n번까지 특정회사는 도로 통해 연결
# 현재 위치 1번, x번 회사에 방문 원함
# 연결된 2개의 회사는 양방향 이동 가능
# 소요 시간은 1
# 1번 회사에서 출발하여 k번 회사를 거쳐 x번 회사로 가는것이 목표(가능한 빠르게) 이동하는 최소 시간 구하기
n,m = map(int, input().split()) # 노드의 개수, 간선의 개수
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트(그래프 번호)를 만들고, 모든 값을 무한으로 초기화

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0



# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1  # A에서 B로 가는 비용은 C라고 설정
    graph[b][a] = 1


x,k = map(int, input().split()) # 도착 노드와 거쳐가는 노드

# k번 노드를 거쳐서 x번 노드 도착
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])


# 놓친 부분
distance = graph[1][k] + graph[k][x]


if distance >= INF:
     print(-1)
else:
     print(distance)







