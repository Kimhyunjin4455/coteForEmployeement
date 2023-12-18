N = int(input())
nums = list(map(int, input().split()))
rs = [1] * (N)


for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            rs[i] = max(rs[i], rs[j]+1)


print(max(rs))
