# 단계마다 '거쳐 가는 노드' 기준으로 알고리즘 수행, 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요는 없음
# 노드의 개수가 n개일때 알고리즘상으로 n번의 단계 수행, 단계마다 O(n^2)의 연산을 통해 현재 노드를 거쳐가는 모든 경로 고려
# 시간 복잡도 => O(N^3)
# 다익스트라는 그리디 알고리즘인거에 반해 플로이드 워셜은 dp, 노드의 개수가 n개일 때 n번 만큼의 단계를 반복하며 점화식에 맞게 2차원 리스트를 갱신
# ex: 1번 노드에 대해서 확인 시 1번 노드를 중간에 거쳐가는 모든 경우 고려, A -> 1 -> B
# ex: 최단 거리 테이블애 A에서 B로 이동하는 비용이 3으로 기록되어 있을 때, 1을 거쳐가는 비용이 2이면 3을 2로 갱신
# 알고리즘에서는 현재 확인하고 있는 노드를 제외하고, n-1개의 노드 중에서 서로 다른 노드(A,B)쌍을 선택
# 이후 A -> 현재 확인 노드 -> B 로 가는 비용 확인 후 최단 거리 갱신

INF = int(1e9)

n = int(input()) # 노드의 개수
m = int(input()) # 간선의 개수

graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트(그래프 번호)를 만들고, 모든 값을 무한으로 초기화

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c # A에서 B로 가는 비용은 C라고 설정

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()


