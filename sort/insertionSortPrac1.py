array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0 , -1): # 인덱스 i부터 0까지 1씩 감소하며 반복
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else: # 작은 데이터를 만나면 멈춤
            break

print(array)
