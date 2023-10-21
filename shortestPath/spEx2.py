# n개의 도시
# 보내고자 하는 메세지가 있을 떄, 다른 도시로 전보를 보내서 다른 도시로 메세지 전송 가능
# 전보 보낼 때는 통로가 설치되어 있어야 함(양방향에 통로가 다 없으면 없는 방향은 메세지 전달 불가), 메세지 보낼 때 일정 시간 소요됨
# c라는 도시에서 출발해 각 도시 사이에 설치된 통로를 통해 최대한 많이 퍼져나가야 함
# 각 도시의 번호와 통로가 설치된 정보가 주어질 때, c에서 보낸 메세지를 받게 되는 도시의 개수는 몇개이며, 걸리는 시간은 얼마인지

import heapq

n,m,c = map(int, input().split()) # 도시의 개수 n 통로의 개수 m 메세지 보내고자 하는 도시 c
INF = int(1e9)


# graph = [[] for i in range(n+1)]
# distance = [[INF] * (n+1) for _ in range(n+1)]

graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화



# 정보를 입력 받아, 연결된 도시에 대해 1차원 리스트에 저장하고 각 도시 간의 거리를 2차원 리스트 저장
for _ in range(m):
    x,y,z = map(int, input().split()) # 도시 x에서 도시 y로 이어지는 통로가 있으며, 전달 시간 z
    graph[x].append((y,z))




def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist: # 현재 노드가 이미 처리된 노드라면 무시
            continue
        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드를 확인
            cost = dist + i[1] # 거리

            if cost < distance[i[0]]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(c)

cnt = 0 # 도달할 수 있는 노드의 개수
max_cost = 0
for d in distance:
    if d != INF:
        cnt += 1
        max_cost = max(d, max_cost)

print(cnt-1, max_cost) # cnt에는 출발 노드도 포함되어 있어서 -1

# re resolve




