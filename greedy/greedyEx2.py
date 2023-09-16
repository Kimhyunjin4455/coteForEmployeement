#풀이(입력 예시 통과)
# n,m = map(int, input().split())
# data = list()
# answer_list = list()
# for _ in range (n):
#     card_list = list(map(int, input().split()))
#     data.append(card_list)
#
# for i in range (len(data)):
#     answer_list.append(min(data[i]))
#
# print(max(answer_list))

#1
# n,m = map(int, input().split())
# result = 0
# for i in range(n):
#     data_1 = list(map(int, input().split()))
#     min_value = min(data_1)
#     result = max(result, min_value)
# print(result)

#2
n,m = map(int, input().split())
result_2 = 0
for i in range(n):
    data_2 = list(map(int, input().split()))
    min_value = 10001 # 입력 조건으로 들어오는 수는 10000 이하이므로 비교를 위해 임의의 수 10001로 설정
    for a in data_2:
        min_value = min(a, min_value)
    result_2 = max(result_2, min_value)
print(result_2)





