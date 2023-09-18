n = int(input())
x, y =1, 1                     # 행,열
move_list = input().split()

# 실제 개념과 달리 풀이에서는 x값이 상하 변경, y값이 좌우 변경
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D'] # L,R이 y값 변경되고 U,D값이 x값 변경됨

for move in move_list:
    for i in range(len(move_types)):
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)