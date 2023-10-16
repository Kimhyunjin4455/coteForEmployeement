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


