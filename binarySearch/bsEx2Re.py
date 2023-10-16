# n,m = map(int, input().split())
# dduck_list = list(map(int, input().split()))
#
# start = 0
# end = max(dduck_list)
#
# result = 0
#
# while(start < end):
#     total = 0
#     mid = (start + end) // 2
#     for x in dduck_list:
#         if x > mid:
#             total += (x-mid)
#     if total > m:
#         start = mid+1
#     else:
#         result = mid
#         end = mid-1
#
# print(result)


n,m = map(int, input().split())
dduck_len = list(map(int, input().split()))

end = max(dduck_len)

def bs(array, target, start, end):

    mid = (start + end) // 2
    product = 0
    for dduck in dduck_len:
        if dduck >= mid:
            product += (dduck-mid)
    if product == m:
        return mid
    elif product > m:
        return bs(array, target, mid+1, end)
    else:
        return bs(array, target, start, mid-1)

print(bs(dduck_len, m, 0, end))







