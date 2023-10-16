# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) +1
#
# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
#
# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column +step[1]
#
#     if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <= 8:
#         result +=1
#
# print(result)


#re resolve
data = input()
row = int(data[1])
column = int(ord(data[0])) -int(ord('a')) + 1 # 입력값이 알파벳이기에 알파벳의 처음인 a를 빼고 1을 더함(시작점이 0이 아닌 1이기 때문)

steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row < 1 or next_row > 8 or next_column <1 or next_column >8:
        continue
    #print(next_row, next_column)
    result +=1

print(result)





