n,m = map(int, input().split())
dduck_len = list(map(int, input().split()))

start = 0
end = max(dduck_len)
result = 0

while(start <= end):
    mid = (start + end) // 2
    total = 0
    for x in dduck_len:
        if x > mid:
            total += (x-mid)

    if total > m:
        start = mid +1
    else:
        result = mid
        end = mid -1

print(result)

