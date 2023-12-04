'''
1. 아이디어
- '매초'번호가 낮은 바이러스부터 증식
- 증식 과정 중 특정 칸에 바이러스가 있다면 그곳에는 증식 불가
- 낮은 번호 부터 bfs
- 제일 중요 --> 바이러스의 초기 상태만 조건에 맞춰 정렬한 뒤 deque으로 변환해 BFS를 구현

2. 시간복잡도
- 200 * 200 * 1000 -> 40000000 -> 가능

3. 자료구조
-
'''

from collections import deque

n, k = map(int, input().split()) # n은 area의 크기, k는 바이러스의 종류(1~k)
area = [list(map(int, input().split())) for _ in range(n)]
s,x,y = map(int, input().split())

time = 0
arr = []
for i in range(n):
    for j in range(n):
        if area[i][j] != 0:
            arr.append([area[i][j], time, i, j])

arr.sort()

dr = [-1,1,0,0]
dc = [0,0,-1,1]

queue = deque(arr)


while queue:

    info = queue.popleft()

    now_virus = info[0]
    now_time = info[1]
    now_row = info[2]
    now_col = info[3]

    if now_time == s:
        break

    for dir in range(4):
        nr = now_row + dr[dir]
        nc = now_col + dc[dir]

        if 0 <= nr < n and 0 <= nc < n:
            if area[nr][nc] == 0:
                area[nr][nc] = now_virus
                queue.append([now_virus, now_time+1, nr, nc])



if area[x-1][y-1] == 0:
    print(0)
else:
    print(area[x-1][y-1])

