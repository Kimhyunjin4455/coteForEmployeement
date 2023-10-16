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
# from collections import deque
#
# n,m = map(int, input().split())
#
# input_data = []
# for i in range(n):
#     input_data.append(list(map(int, input())))
#
# dx = [-1, 1, 0, 0]
# dy = [0,0,-1,1]
#
# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >=m: #미로 찾기 공간을 넘어선 경우
#                 continue
#             if input_data[nx][ny] ==0:
#                 continue
#
#             if input_data[nx][ny] == 1:
#                 input_data[nx][ny] = input_data[x][y] +1 # 인접 노드 체크와 방문 횟수를 한번에 처리
#                 queue.append((nx, ny))
#         return input_data[n-1][m-1]
#
# print(bfs(0,0))

# re resolve2
# from collections import deque
# n,m = map(int, input().split())
# input_data = []
# count_list = [[0]*m for _ in range(n)]
# visited_list = [[0]*m for _ in range(n)]
# for _ in range(n):
#     input_data.append(list(map(int, input())))
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# count_list[0][0] = 1
# visited_list[0][0] = 1
#
#
# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if input_data[nx][ny] == 0: #에리어 바깥 외에 갈수 없는 경우
#                 continue
#             if input_data[nx][ny] == 1 and visited_list[nx][ny] ==0:
#                 queue.append((nx, ny))
#                 visited_list[nx][ny] =1
#                 count_list[nx][ny] = count_list[x][y] + 1
#
#
#
#     return count_list[n-1][m-1]
# print(bfs(0,0))

#re resolve3

from collections import deque

n,m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

if_visited = [[0] * m for _ in range(n)]
visited_cnt = [[0] * m for _ in range(n)]
if_visited[0][0] = 1
visited_cnt[0][0] = 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue: # 이 코드가 빠지면 queue가 빈 상태에서 popleft()를 진행해서 에러 발생
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1 and if_visited[nx][ny] == 0:
                queue.append((nx,ny))
                if_visited[nx][ny] = 1
                visited_cnt[nx][ny] = visited_cnt[x][y] + 1

    return visited_cnt[n-1][m-1]


print(bfs(0,0))
