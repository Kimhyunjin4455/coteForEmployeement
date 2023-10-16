# n = int(input())
# array = []
# for i in range(n):
#     input_data = input().split()
#     array.append((input_data[0], int(input_data[1]))) # 이름은 문자열 그대로, 정수는 정수형으로 변환해 저장
#
# # array.sort(array, key=lambda student: student[1])
# #
# # for student in array:
# #     print(student[0], end=' ')
#
# def setting(data):
#     return data[1]
#
# result = sorted(array, key=setting)
#
# for i in result:
#     print(i[0], end=' ')
#


n = int(input())
array = []

for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    array.sort(key=lambda array:array[1])

for i in range(len(array)):
    print(array[i][0], end=" ")

