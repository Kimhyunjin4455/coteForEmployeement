# 퀵 정렬:
# 1. 리스트에서 첫 데이터를 피벗으로 정함
# 2. 왼쪽에서부터 피벗보다 큰 데이터 찾고, 오른쪽에서부터 피벗보다 작은 데이터 찾음
# 3. 큰 데이터와 작은 데이터의 위치 교환, 이러한 과정 수행시 피벗에 대하여 정렬이 수행됨
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left +=1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -=1
        # 엇갈렸다면, 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
        else:
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1)
    quick_sort(array, right +1, end)

quick_sort(array, 0, len(array)-1)
print(array)

