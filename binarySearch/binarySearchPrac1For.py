def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) //2
        print(array[start], array[end])
        if array[mid]==target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    print(start, end)
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)  # 현재 위치 반환.(인덱스는 0부터 시작해서 +1)

