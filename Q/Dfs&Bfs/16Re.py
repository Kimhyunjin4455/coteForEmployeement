# '''
# 1. 아이디어
# - 0은 빈칸, 1은 벽, 2는 바이러스
# - 벽이 없다면 바이러스는 빈칸으로 퍼져 나감
# - 이중 for 문으로 모든 칸 진행하면서 상하좌우가 1이면 그만 (방문여부 체크하여 시간낭비 해소)
# - Dfs&Bfs 통해 2로 변경하고 마지막에 0의 개수를 반환
# - 벽을 3개 세워야 함 -> 각각 다른 벽이 세워진 area로 Dfs&Bfs 진행 후 안전영역 반환 -> 결과에 저장(큰 값일때 값 저장)
#
# 2. 시간복잡도
# - v+e -> 5v -> 5*64 -> 가능
#
# 3. 자료구조
# - area [[],[],...]
# - chk [[False] * (v)]
# '''


n,m = map(int, input().split())
area = []
temp = [[0] * m for _ in range(n)]

for i in range(n):
    area.append(list(map(int, input().split())))
# area값의 유지를 위해 벽 값을 입력할 배열 새로 생성

dr = [-1,1,0,0]
dc = [0,0,-1,1]

result = 0

def virus(row,col):
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr and nr < n and 0 <= nc and nc < m: # 범위 내에서
            if temp[nr][nc] == 0: # 바이러스 퍼트릴 수 있으면
                temp[nr][nc] = 2
                virus(nr, nc)

def get_score():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt

def dfs(num):
    global result
    if num == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = area[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return


    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:
                area[i][j] = 1
                num += 1
                dfs(num)
                area[i][j] = 0
                num -= 1


dfs(0)
print(result)


# n, m = map(int, input().split())
#
# area = []  # 초기 맵 리스트
# temp = [[0] * m for _ in range(n)]
#
# for _ in range(n):
#     area.append(list(map(int, input().split())))
#
# # 상하좌우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# result = 0
#
#
# # DFS로 바이러스 퍼지게 하기
# def virus(row, col):
#     for i in range(4):
#         nr = row + dr[i]
#         nc = col + dc[i]
#         # 상하좌우 중에서 바이러스가 퍼질 수 있는 경우
#         if nr >= 0 and nr < n and nc >= 0 and nc < m:
#             if temp[nr][nc] == 0:
#                 # 해당 위치에 바이러스 배치하고, 재귀적으로 수행
#                 temp[nr][nc] = 2
#                 virus(nr, nc)
#
#
# # 현재 맵에서 안전 영역의 크기 계산
# def get_score():
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 cnt += 1
#     return cnt
#
#
# # DFS를 이용하여 울타리를 설치하면서, 매번 안전 영역의 크기 계산
# def Dfs&Bfs(num):
#     global result
#     # 울타리가 3개 설치된 경우
#     if num == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = area[i][j]
#
#         # 각 바이러스의 위치에서 전파 진행
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i, j)
#
#         # 안전 영역의 최대값 계산
#         result = max(result, get_score())
#         return
#
#
#     for i in range(n):
#         for j in range(m):
#             if area[i][j] == 0:  # 빈 공간 일 때
#                 area[i][j] = 1  # 벽 세우고
#                 num += 1  # 벽 세울 때 마다 count +=1
#                 Dfs&Bfs(num)  # 다음 벽 세우기 위해 Dfs&Bfs
#                 area[i][j] = 0  # 재귀 풀리는 과정 세웠던 벽 지우고
#                 num -= 1  # 카운트도 복귀
#
#
# Dfs&Bfs(0)
# print(result)
