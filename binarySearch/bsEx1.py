# n = int(input())
# stock_list = list(map(int, input().split()))
#
# m = int(input())
# wish_list = list(map(int, input().split()))
#
# stock_list.sort()
#
# answer = []
#
# def binary_search(stock_list, target, start, end): # target에 대해 생각 못했음
#     while(start<= end):
#         mid = (start + end) // 2
#         if stock_list[mid] == target:
#             return 1
#         elif stock_list[mid] < target:
#             start = mid +1
#         else:
#             end = mid -1
#     return None
#
#
#
# for wish_list_item in wish_list:
#     result = binary_search(stock_list, wish_list_item, 0, n-1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')



def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return 'no'

    elif array[mid] == target:
        return 'yes'

    elif array[mid] > target:
        return binary_search(array, target, start, mid-1) # 여기서 return 없이 호출만 할 경우 함수 내부의 리턴값이 있더라도 none으로 반환됨?

    else:
        return binary_search(array, target, mid+1, end)
    # 2 3 7 8 9 (0,4)
    # 5, 2 3 7 (0,1) -> binary_search(array, target, 2,1) -> return 'no'

n = int(input())
stock_list = sorted(list(map(int, input().split())))

m = int(input())
wish_list = sorted(list(map(int, input().split())))



for wish in wish_list:
    print(binary_search(stock_list, wish, 0, n-1), end=' ')

# def bin_search(arr, target, start, end):
#     mid = (start + end) // 2  # 중간점(index) 설정
#     if start > end:  # 타겟이 없을 경우
#         return 'no'
#
#     elif arr[mid] == target:  # 타겟을 찾음
#         return 'yes'
#
#     elif arr[mid] > target:  # 중간점이 타겟보다 크다면
#         return bin_search(arr, target, start, mid - 1)
#
#     else:  # 중간점이 타겟보다 작다면
#         return bin_search(arr, target, mid + 1, end)
#
#
# n = int(input())
# arr = sorted(list(map(int, input().split())))
# m = int(input())
# order = sorted(list(map(int, input().split())))
#
# for target in order:
#     print(bin_search(arr, target, 0, n - 1), end=' ')