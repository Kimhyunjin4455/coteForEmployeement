N,L,R = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]* N for _ in range(N)]
peoples = 0
result = 0
dr = [1,-1,0,0]
dc = [0,0,-1,1]


def dfs(i, j):
    global peoples
    global result
    global recur

    row = i
    col = j

    visited[i][j] = True
    peoples += area[row][col]

    for dir in range(4):
        nr = row + dr[dir]
        nc = col + dc[dir]
        if 0 <= nr <N and 0 <= nc < N:
            if (visited[nr][nc] == False) and L <= abs(area[row][col] - area[nr][nc]) <= R:
                recur.append(0)
                dfs(nr, nc)

    area[row][col] = int(peoples/len(recur))
    # visited[row][col] = False
    return True





for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            peoples = 0
            recur = [0]
            for k in range(N):
                for l in range(N):
                    visited[k][l] = False

            for dir in range(4):
                nr = i + dr[dir]
                nc = j + dc[dir]
                if 0 <= nr < N and 0 <= nc < N:
                    if (visited[nr][nc] == False) and L <= abs(area[i][j] - area[nr][nc]) <= R:
                        dfs(i,j)
                        result += 1

print(result)
