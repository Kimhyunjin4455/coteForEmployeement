# # n가지 종류의 화폐, 최소한 이용해서 합이 M원이 되도록, 화폐 중복 사용 o, 순서 다른 경우는 같은 경우로 취급
# # 2원 과 3원이 있을때 합이 15원이 되도록 최소한 이용하는 것은 3원만 5번 사용
#
# n,m = map(int, input().split())
# coin = []
# for _ in range(n):
#     coin.append(list(map(int, input().split())))
#
# dp = [10001] * (m+1)
# dp[0] = 0
#
#
# for i in range(n):
#     for j in range(coin[i], m+1):
#         if dp[j-coin[i]] != 10001: # ex: 2 -> dp[0] 0 dp[1] 10001 dp[2] 1 (0+1) dp[3] 10001 dp[4] 2 (1+1)
#             dp[j] = min(dp[j], dp[j-coin[i]]+1)
#
# if dp[m] == 10001:
#     print(-1)
# else:
#     print(dp[m])

# re resolve
# 적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수 찾기
n,m = map(int, input().split())
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))

dp = [10001] * (m+1) # 10001은 특정 금액을 만들 수 있는 화폐구성이 가능하지 않다는 의미
dp[0] = 0

for i in range(n):
    for j in range(coin_list[i], m+1):
        dp[j] = min(dp[j], dp[j-coin_list[i]]+1)

print(dp[m])











