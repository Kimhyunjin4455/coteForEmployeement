# '''
# 1. 아이디어
# - 만들 수 있는 식의 최댓값과 최솟값 출력
# - 연산횟수를 줄여가며 백트래킹
#
# 2. 시간복잡도
#
# 3. 자료구조
# '''
#
# N = int(input())
# nums = list(map(int, input().split()))
# add_cnt, sub_cnt, mul_cnt, div_cnt = map(int, input().split())
#
#
# # 연산 횟수를 줄여가며 카운트
# max_value = int(-1e9)
# min_value = int(1e9)
#
# def calculator(i, value):
#
#     global add_cnt, sub_cnt, mul_cnt, div_cnt, max_value, min_value
#     if i == N:
#         max_value = max(max_value, value)
#         min_value = min(min_value, value)
#
#
#     else:
#         if add_cnt > 0:
#             add_cnt -= 1
#             calculator(i+1, value + nums[i])
#             add_cnt += 1
#         if sub_cnt > 0:
#             sub_cnt -= 1
#             calculator(i+1, value - nums[i])
#             sub_cnt += 1
#         if mul_cnt > 0:
#             mul_cnt -= 1
#             calculator(i+1, value * nums[i])
#             mul_cnt += 1
#         if div_cnt > 0:
#             div_cnt -= 1
#             calculator(i+1, int(value / nums[i]))
#             div_cnt += 1
#
#
# # int(a/b)와 a//b의 차이는 a//b는 나눈 값을 내림처리를 진행하지만, int()는 소수점을 버리는 처리의 차이가 존재
#
# calculator(1, nums[0])
# print(max_value)
# print(min_value)
#
