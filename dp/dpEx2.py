n = int(input())
container = list(map(int, input().split()))

dp = [0] * 100

dp[0] = container[0]
dp[1] =max(container[0], container[1]) # 둘중에 큰것을 털어야함

# 3 1 1 5

for i in range(2,n): #세번째 부터는 인접하지 않은 규칙을 적용해 점화식대로 값 구함
    dp[i] = max(dp[i-1], dp[i-2]+container[i])

print(dp[n-1])