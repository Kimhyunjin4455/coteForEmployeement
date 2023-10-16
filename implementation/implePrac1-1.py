# n = int(input())
# move_list = input().split()
# x,y =1, 1
#
# move_type = ['L','R','U','D']
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
#
# for move in move_list:
#     for i in range(len(move_list)):
#         if move == move_list[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
#
# print(x,y)
#

n = int(input())
data = input().split()
x,y = 1,1

dx = [0,0,-1,1] # up경우 좌표값 -1, down경우 좌표값 +1
dy = [-1,1,0,0]
direction = ['L', 'R', 'U', 'D']

nx, ny = 0, 0

for plan in data:
    for i in range(4):
        if plan == direction[i]:
            nx = x +dx[i]
            ny = y +dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n: # U로 인해 nx값이 0이 된 경우
        continue
    x = nx
    y = ny

print(x,y)



