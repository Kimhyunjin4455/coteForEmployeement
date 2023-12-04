# n,m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# def Dfs&Bfs(x,y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         Dfs&Bfs(x-1, y)
#         Dfs&Bfs(x, y-1)
#         Dfs&Bfs(x+1, y)
#         Dfs&Bfs(x, y+1)
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if Dfs&Bfs(i,j) == True:
#             result += 1
#             print(i,j)
#
# print(result)


# re resolve
n,m = map(int, input().split())
input_data = []
for _ in range(n):
    input_data.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: # 범위 제한
        return False
    if input_data[x][y] == 0: # 방문하지 않았을 경우
        input_data[x][y] = 1 # 방문 처리
        dfs(x-1, y) # 상하좌우 재귀호출
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: # 순차적으로 가더라도 구역의 처음만 result +=1 되고 그 외에는 def dfs의 if문의 방문 여부에서 걸러짐
            result +=1

print(result)



