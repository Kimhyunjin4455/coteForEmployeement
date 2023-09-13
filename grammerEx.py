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
