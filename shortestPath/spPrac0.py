# 최단 경로 문제는 보통 그래프를 이용해 표현
# 다익스트라 최단 경로 알고리즘: 1출발 노드 설정 -> 2최단 거리 테이블 초기화 -> 3방문하지 않은 노드중 최단 거리의 노드 선택
# -> 4해당 노드를 거쳐 다른 노드로 가는 비용 계산, 최단 거리 테이블 갱신 -> 위 과정의 3/4 반복
# 다익스트라 알고리즘은 최단 경로를 구하는 과정에서 '각 노드에 대한 현재까지의 최단 거리' 정보를 항상 1차원 리스트에 저장하며 계속 갱신

# 출발 노드 설정, 출발 노드에서 다른 모든 노드로의 최단 거리 계산, 초기 상태에서 다른 모든 노드로 가는 최단 거리를 무한으로 설정
# 0. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택(출발 노드 -> 출발 노드 의 거리는 0, 출발 노드가 선택됨)
# 출발 노드를 거쳐 다른 노드로 가는 비용 계산(출발 노드와 연결된 모든 간선을 하나씩 확인), 더 짧은 경로를 찾았으니 최단 거리 리스트의 무한 값을 최단 거리 값으로 갱신
# 이후의 단계에서 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택(같은게 여럿 있으면 번호가 작은 노드 선택), 이후 이전의 과정 반복
# 이후의 과정 중 N번 노드의 새로운 비용을 구했더라도 최단 거리 테이블에서 N번 노드까지의 최단 거리 값이 있기에 값이 갱신되지 않음
# 다익스트라 알고리즘이 진행되면서 한 단계 당 하나의 노드에 대한 최단 거리를 확실히 찾음


# 간단한 다익스트라 알고리즘
# O(v^2)의 시간복잡도, v는 노드의 갯수
# 각 노드의 최단 거리를 담는 1차원 리스트 선언, 이후 단계마다 방문하지 않은 노드중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소 확인(순차 탐색)
# bfs/Dfs&Bfs 와 마찬가지로 모든 리스트는 (노드의 갯수 +1)로 할당 -> 노드의 번호를 인덱스로 하여 바로 리스트에 접근할 수 있도록 설정(그래프 표현 시 많이 사용하는 일반적인 코드)

import sys # 입력되는 데이터의 수가 많다는 가정히에 input()을 더 빠르게 동직하는 sys.stdin.readline 으로 치환
input = sys.stdin.readline()
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n,m = map(int, input.split()) # 노드의 갯수, 간선의 갯수
start = int(input()) # 시작 노드 번호 입력받기
graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n+1)
distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m): # 모든 간선 정보 입력받기
    a,b,c = map(int, input.split()) # a번 노드에서 b번 노드로 가는 비용이 C라는 의미
    graph[a].append((b,c))

def get_smallest_node():# 방문하지 않은 노드 중에서, 가장 최단 거리의 노드 반환
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    distance[start] = 0 # 시작 노드에 대해 초기화
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # j[0]은 노드번호 j[1]은 거리

    for i in range(n-1): # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
        now = get_smallest_node() # 현재 최단 거리가 가장 짧은 노드를 꺼내 방문 처리
        visited[now] = True
        for j in graph[now]: # 현재 노드와 연결된 다른 노드를 확인
            cost = distance[now] + j[1]
            if cost < distance[j[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1): #모든 노드로 가기 위한 최단 거리 출력
    if distance[i] == INF: # 도달할 수 없는 경우, 무한 출력
        print("INFINITY")
    else:
        print(distance[i])



