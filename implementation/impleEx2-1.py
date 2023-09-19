n,m = map(int, input().split())
a,b,direction = map(int, input().split())
d = [[0]*m for _ in range(n)] # 방문한 장소 저장 위한 것
d[a][b] = 1

da = [-1, 0, 1, 0] # 상하조절은 d[a]범위
db = [0, 1, 0, -1] # 좌우조절은 d[a][b] 범위

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    na = a + da[direction]
    nb = b + db[direction]

    if d[na][nb] == 0 and array[na][nb] == 0:
        d[na][nb] = 1
        a = na
        b = nb
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    if turn_time == 4:
        na = a - da[direction]
        nb = b - db[direction]

        if array[na][nb] == 0:
            a = na
            b = nb

        else:
            break
        turn_time = 0

print(count)
