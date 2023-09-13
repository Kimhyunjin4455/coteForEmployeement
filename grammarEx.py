import sys
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

#1
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

#2
b = 0.3 + 0.9
print(b)

if b == 1.2:
    print(True)
else:
    print(False)

#3
array1 = [i*i for i in range(1,10)]
print(array1)

#4
n=3
m=4
array2 = [[0] * m for _ in range(n)]
print(array2)

#5-1
n=3
m=4
array3 = [[0]*m]*n
array3[1][1] = 5
print(array3) # 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식됨

#5-2
n=3
m=4
array4 = [[0] * m for _ in range(n)]
array4[1][1] = 5
print(array4)

#6
list_a = [1,2,3,4,5,5,5,]
remove_set = {3,5}

result_a = [i for i in list_a if i not in remove_set]
print(result_a)

#7
data_1 = "Don't you know \"Python\""
print(data_1)

#8
data_2 = dict()
data_2['아이폰14Pro'] = 'A16'
data_2['아이폰15'] = 'A16'
data_2['아이폰15Pro'] = 'A17Pro'
print(data_2)
if '아이폰15' in data_2:
    print("'아이폰15'를 키로 가지는 데이터가 존재합니다.")
key_list = data_2.keys()
value_list = data_2.values()
print(key_list)
print(value_list)
for key in key_list:
    print(data_2[key])

#9
a_9 = set([1,2,3,3,3,4,4,5,6,7])
print(a_9)
b_9 = {1,2,2,3,4,4,5}
print(b_9)

print(a_9 | b_9) # 합집합
print(a_9 & b_9) # 교집합
print(a_9 - b_9) # 차집합

a_9.add(8)
print(a_9)
b_9.update([6,7])
print(b_9)
b_9.remove(2)
print(b_9)

#10
score_10 = 85
if score_10 >= 80:
    pass
else:
    print("80미만")
print("종료합니다.")

#10-1
score_101 = 85
result_101 = "success" if score_101 >=80 else "fail"
print(result_101)

#11
scores_11 = [90, 85, 77, 65, 97]
cheating_list = {2,4}
for i in range(5):
    if i+1 in cheating_list:
        continue
    if scores_11[i] >= 80:
        print(i+1, "번님 합격")

#12
a_11 = 0
def func_11():
    global a_11
    a_11 += 1
for i in range(10):
    func_11()

print(a_11)

#13
print((lambda a,b: a+b)(3,7))

#14
# n_14 = int(input()) # 데이터의 개수 입력
# data_14 = list(map(int, input().split())) # 각 데이터를 공백으로 구분하여 입력
# data_14.sort(reverse=True)
# print(data_14)

#14-1
# n_14, m_14, k_14 = map(int, input().split())
# print(n_14,m_14,k_14)
#
#15
# data_15 = sys.stdin.readline().rstrip() # readline() 입력하면 입력 후 엔터가 줄바꿈 기호로 입력되는데, 이를 제거하기 위해 rstrip()사용
# print(data_15)

#16
answer_16 = 8
print("정답은 " + str(answer_16) + " 입니다.")
print("정답은",answer_16,"입니다.") # 각 변수를 콤마로 구분하는 경우 의도치 않은 공백이 삽입될 수 있음
print(f"정답은 {answer_16} 입니다.")

#17
result_17 = eval("(3+5)*7")
print(result_17)

#18
result_18 = sorted([('아이폰13', 2021), ('아이폰14', 2022), ('아이폰15', 2023)], key = lambda x: x[1], reverse=True)
print(result_18)

#19
data_19 = ['A', 'B', 'C']
result_19 = list(permutations(data_19, 3)) #모든 순열 구하기, 리스트에서 3개를 뽑아 나열하는 모든 경우의 수
print(result_19)
result_19_1 = list(combinations(data_19, 2)) #순서를 고려하지 않고 나열하는 모든 경우의 수
print(result_19_1)
result_19_2 = list(product(data_19, repeat=2)) #2개를 뽑아 나열하되 원소를 중복하여 뽑음
print(result_19_2)
result_19_3 = list(combinations_with_replacement(data_19, 2)) #순서를 고려하지 않고 나열하는 모든 경우의 수 + 원소를 중복으로 뽑음
print(result_19_3)