n,m = map(int, input().split())
dduck_list = list(map(int, input().split()))

start = 0
end = max(dduck_list)

result = 0

while(start < end):
    total = 0
    mid = (start + end) // 2
    for x in dduck_list:
        if x > mid:
            total += (x-mid)
    if total > m:
        start = mid+1 #자를 길이를 더 뒤로 설정해야함
    else: # start가 m보다 같거나 작을 경우
        result = mid # 같을 경우를 대비해 값 저장
        end = mid - 1 #자를 길이의 기준을 더 앞으로 설정해야 함(자른 길이가 더 많아지도록 설정)



print(result)



# n,m = map(int, input().split())
# dduck_len = list(map(int, input().split()))
#
# end = max(dduck_len)
#
# def bs(array, target, start, end):
#
#     mid = (start + end) // 2
#     product = 0 # 자른 길이의 합
#     # 각 떡의 길이에 대해
#     for dduck in dduck_len:
#         if dduck >= mid: # 떡의 길이가 중간값보다 크면(자를 수 있으면)
#             product += (dduck-mid) # 총 길이에 더함
#     if product == m: # 길이가 딱 맞으면 중간값 반환
#         return mid
#     elif product > m: # 길이가 크면 기준을 뒤로 설정(뒤로 설정해야 자르는 떡의 길이의 합이 작아음)
#         return bs(array, target, mid+1, end)
#     else: # 길이가 짧으면 기준을 앞으로 설정
#         return bs(array, target, start, mid-1)
#
# print(bs(dduck_len, m, 0, end))
