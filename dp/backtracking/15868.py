# 크기가 N×N인 도시, 1×1크기의 칸으로 나뉨
# 각 칸은 0빈 칸, 2치킨집, 1집 중 하나
# 도시의 칸은 (r, c)와 같은 형태, r과 c는 1부터 시작
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리 (집을 기준으로 정해짐)
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합
# 치킨 거리 계산 시 abs(rowA - rowB) + abs(colA - colB)
# 도시에 있는 치킨집 중에서 최대 M개를 고르기 (도시의 치킨 거리가 가장 작게)

n,m = map(int, input().split()) # m은 치킨집 의미
area = [list(map(int, input().split())) for _ in range(n)]
res = 1e9

def dfs(cnt):
    if cnt == m:


        res = min(res, )

    for i in range(n):
        for j in range(n):
            if area[i][j] == 1:




