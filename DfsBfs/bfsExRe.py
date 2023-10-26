# # from collections import deque
# #
# # n,m = map(int, input().split())
# # graph = []
# #
# # for _ in range(n):
# #     graph.append(list(map(int, input())))
# #
# # dx = [-1, 1, 0, 0]
# # dy = [0,0,-1,1]
# #
# # def bfs(x,y):
# #
# #     queue = deque()
# #     queue.append((x,y))
# #
# #     while queue:
# #         x, y = queue.popleft()
# #
# #         for i in range(4):
# #             nx = x + dx[i]
# #             ny = y + dy[i]
# #
# #             if nx <0 or nx >=n or ny <0 or ny >= m: # 미로 공간을 벗어난 경우
# #                 continue
# #             if graph[nx][ny] == 0: # 미로의 벽을 만난 경우
# #                 continue
# #
# #             if graph[nx][ny] == 1:
# #                 graph[nx][ny] = graph[x][y]+1
# #                 queue.append((nx,ny))
# #
# #     return graph[n-1][m-1]
# #
# #
# # print(bfs(0,0))
#
# from collections import deque
#
# n,m = map(int, input().split())
# maze = []
# for _ in range(n):
#     maze.append(list(map(int, input())))
#
#
# visited = [[0]*m for _ in range(n)]
# time = [[0]*m for _ in range(n)]
#
# visited[0][0] = 1
# time[0][0] = 1
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x, y = queue.popleft() # for문 안에서 시도하면 queue가 빈채로 popleft가 진행될수도 있음
#         for i in range(4):
#
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if maze[nx][ny] == 0:
#                 continue
#             if maze[nx][ny] == 1 and visited[nx][ny] == 0:
#                 queue.append((nx,ny))
#                 visited[nx][ny] = 1
#                 time[nx][ny] = time[x][y] + 1
#                 continue
#
#     return time[n-1][m-1]
#
# print(bfs(0,0))
#


from collections import deque

n,m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

visit_list = [[0]*m for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visit_list[x][y] = 1

    while queue: #
        x,y = queue.popleft() #

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or nx >= n or ny < 0 or ny >= m ):
                continue
            if maze[nx][ny] == 0:
                continue

            if (maze[nx][ny] == 1 and visit_list[nx][ny] == 0):
                visit_list[nx][ny] = visit_list[x][y]+ 1
                queue.append((nx, ny))


    return visit_list[n-1][m-1]

print(bfs(0,0))
























