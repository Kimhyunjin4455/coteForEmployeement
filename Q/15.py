# 1~N번 도시, M개 단방향 도로
# 특정 도시 x로 부터 출발하여 도달할 수 있는 모든 도시 중에서 '최단 거리'가 정확히 k 인 모든 도시 번호 출력

import sys
# input = sys.stdin.readline()

from collections import deque

n,m,k,x = map(int, input().split())
visited = [[] for _ in range(n+1)] # [[] *(n+1)] 차이 뭔지

for i in range(m):
    a,b = map(int, input().split())
    visited[a].append(b)

distance = [[-1] * (n+1)] # 최단 거리 초기화
distance[x] = 0

queue = deque()
queue.append(x)

cnt = 0

while queue:
    v = queue.popleft()
    for i in visited[v]:
        if distance[i] < distance[v] + 1:
            distance[i] = distance[v] + 1
            queue.append(i)

for result in range (len(distance)):
    if distance[result] == k:
        print(result)
else:
    print(-1)
print(visited)

