# 캐릭터는 1x1크기의 정사각형으로 이뤄진 NxM의 직사각형
# 상하좌우 움직임, 바다 진입 불가
# 1- 현재 위치에서 현재 방향을 기준으로 왼쪽부터 차례대로 갈 곳 정함
# 2- 캐릭터의 바로 왼쪽 방향에 가보지 않은 칸이 존재하면, 왼쪽 방향으로 회전 후 왼쪽으로 한칸 전진, 왼쪽 방향에 가보지 않은 칸 없으면 회전만 하고 1 로 돌아감
# 3- 네 방향 모두 가봤거나 바다면, 방향 유지한채로 한 칸 뒤로 가고 1단계로 돌아감(뒤쪽도 바다이면 움직임 멈춤)

n,m = map(int, input().split())

d = [[0]*m for _ in range(n)]

x,y,direction = map(int, input().split())

d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽 회전
def turn_left():
    global direction
    direction -=1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count +=1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)
