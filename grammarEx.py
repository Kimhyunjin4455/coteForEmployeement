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
