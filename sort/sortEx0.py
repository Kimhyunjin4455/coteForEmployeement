# 기본 정렬 라이브러리 sorted()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

# 리스트 객체 내장 함수 sort()
array_2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array_2.sort()
print(array_2)

# 정렬 시 key 매개변수 입력받기(key값으로는 하나의 함수가 들어가야 하며, 정렬 기준이 됨)

# 예시는 튜플로 구성된 리스트
array_3 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result_3 = sorted(array_3, key=setting)
print(result_3)