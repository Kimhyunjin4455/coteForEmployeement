# n가지 종류의 화폐, 최소한 이용해서 합이 M원이 되도록, 화폐 중복 사용 o, 순서 다른 경우는 같은 경우로 취급
# 2원 과 3원이 있을때 합이 15원이 되도록 최소한 이용하는 것은 3원만 5번 사용

n,m = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(list(map(int, input().split())))

dp = [10001] * (m+1)
dp[0] = 0


for i in range(n):
    for j in range(coin[i], m+1):
        if dp[j-coin[i]] != 10001:
            dp[j] = min(dp[j], dp[j-coin[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])