n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
INF = 1e9
res = INF



def dfs(depth, idx):
    global res
    if depth == n//2:
        teamA = 0
        teamB = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    teamA += nums[i][j]
                elif not visited[i] and not visited[j]:
                    teamB += nums[i][j]
        res = min(res, abs(teamA - teamB))
        return


    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0,0)
print(res)

