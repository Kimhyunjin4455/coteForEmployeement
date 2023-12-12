from collections import deque

N,L,R = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]


ans = 0
union_lst = []
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    union_lst = [(i, j)]
    peoples = area[i][j]

    while queue:
        now_row, now_col = queue.popleft()

        for dir in range(4):
            nr = now_row + dr[dir]
            nc = now_col + dc[dir]
            if 0 <= nr < N and 0 <= nc < N and (visited[nr][nc] == False):
                if L <= abs(area[now_row][now_col] - area[nr][nc]) <= R:
                    queue.append((nr,nc))
                    visited[nr][nc] = True
                    peoples += area[nr][nc]
                    union_lst.append((nr,nc))

    for (row,col) in union_lst:
        area[row][col] = int(peoples/len(union_lst))

    if len(union_lst) > 1:
        return True

    return False




while ans <= 2000:
    visited = [[False] * N for _ in range(N)]
    flag = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                t = bfs(i,j)     #
                if t == True:       #
                    flag = 1     # 위 세줄을 t = max(t, bfs(i,j)) 로 치환 가능


    if flag == 0:
        break
    ans += 1

print(ans)
