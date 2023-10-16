# n,k = map(int, input().split())
# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))
#
# a_list.sort()
# b_list.sort(reverse=True)
#
# for i in range(k):
#     if(a_list[i] < b_list[i]):
#         a_list[i] = b_list[i]
#     else:
#         break
#
# print(sum(a_list))


n,k = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()
array_b.sort(reverse=True)

for i in range(k):
    if array_a[i] < array_b[i]:
        array_a[i], array_b[i] = array_b[i], array_a[i]
    # else: # else문 없어도 작동
    #     break # 오름차순 정렬의 값이 내림차순 정렬의 값보다 크다면 그 이후는 계산 X,

print(sum(array_a))