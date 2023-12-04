from collections import deque
# import sys
# input = sys.stdin.readline()

n,m,k,x = map(int, input().split())
area = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    area[a].append(b)

def bfs(x):
    queue = deque()
    queue.append(x)
    distance[x] = 0

    while queue:
        now = queue.popleft()
        for next in area[now]:
            if distance[next] == -1:
                distance[next] = distance[now] + 1
                queue.append(next)

    for i in range(len(distance)):
        if distance[i] == k:
            print(i)
    else:
        if k not in distance:
            print(-1)

bfs(x)


