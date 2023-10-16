# from collections import deque
#
# n,m = map(int, input().split())
# maze = []
# for _ in range(n):
#     maze.append(list(map(int, input())))
#
# # 이동할 네 방향 정의
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#
#
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#
#             if maze[nx][ny] == 0:
#                 continue
#
#             if maze[nx][ny] == 1:
#                 maze[nx][ny] = maze[x][y] + 1
#                 queue.append((nx,ny))
#     return maze[n-1][m-1]
#
# print(bfs(0,0))

# re resolve, 위치 옮겨갈때 자리마다 숫자 올려주는 개념 중요
from collections import deque

n,m = map(int, input().split())

input_data = []
for i in range(n):
    input_data.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >=m: #미로 찾기 공간을 넘어선 경우
                continue
            if input_data[nx][ny] ==0:
                continue

            if input_data[nx][ny] == 1:
                input_data[nx][ny] = input_data[x][y] +1 # 인접 노드 체크와 방문 횟수를 한번에 처리
                queue.append((nx, ny))
        return input_data[n-1][m-1]

print(bfs(0,0))

# re resolve2