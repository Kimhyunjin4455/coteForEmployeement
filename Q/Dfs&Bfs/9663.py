# 퀸은 좌우/상하/대각선 모두 이동 가능
# 백트래킹
N = int(input())
area = [0] * N
ans = 0

def going(row):
    for i in range (row):
        if area[row] == area[i] or abs(area[row]-area[i]) == abs(row-i):
            return False
    return True


def dfs(count):
    global ans
    if count == N:
        ans += 1

    else:
        for now_row in range(N):
            area[count] = now_row # 행 인덱스값에다가 열을 저장
            if going(count): # 퀀을 더 놓을 수 있다면
                dfs(count+1)

dfs(0)
row = [0] * N
#
#
# def is_promising(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
#             return False
#
#     return True
#
#
# def n_queens(x):
#     global ans
#     if x == N:
#         ans += 1
#
#     else:
#         for i in range(N):
#             # [x, i]에 퀸을 놓겠다.
#             row[x] = i
#             if is_promising(x):
#                 n_queens(x + 1)
#
#
# n_queens(0)
print(ans)

