n = int(input())
move_list = input().split()
x,y =1, 1

move_type = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for move in move_list:
    for i in range(len(move_list)):
        if move == move_list[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x,y)

