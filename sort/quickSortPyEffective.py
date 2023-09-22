array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이상의 원소를 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# ‘5’ left 0 3 1 2 4 right 7 9 6 8
# (Left)
# ‘0’ right 3 1 2 4
# ‘3’ left 1 2 right 4
# ‘1’ right 2  >> left_side가 없어서 1 2 리턴
# 1 2 + 3 + 4
# 0 + 1 2 3 4
# (right)
# ‘7’ left 6 right 9 8
# 6은 원소가 한개인 리스트라 리턴 > 6 + 7
# ‘9’ left 8 >> 8 + 9 리턴
# 6 + 7 + 8 + 9
# 최종 left_side 1 2 3 4 pivot 5 right side 6 7 8 9