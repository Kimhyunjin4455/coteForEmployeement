# n = int(input())
#
# dp = [0] * 1001
#
# dp[1] = 1 # 2x1 은 한가지의 경우로 만들어짐
# dp[2] = 3 # 2x2 는 세가지의 경우로 만들어짐 ( 2x1 2개, 1x2 2개, 2x2 1개)
#
# for i in range(3, n+1): # 이 문제의 점화식에선 i-1의 경우( 2x1 한가지만 추가) i-2의 경우 두가지(1x2 2개, 2x2 1개)를 더하는 것이 핵심
#     dp[i] = (dp[i-1] + dp[i-2]*2) % 796796
#
# print(dp[n])

# re resolve

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1] + (dp[i-2]*2)) % 796796

print(dp[n])











