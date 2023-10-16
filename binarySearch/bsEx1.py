n = int(input())
stock_list = list(map(int, input().split()))

m = int(input())
wish_list = list(map(int, input().split()))

stock_list.sort()

answer = []

def binary_search(stock_list, target, start, end): # target에 대해 생각 못했음
    while(start<= end):
        mid = (start + end) // 2
        if stock_list[mid] == target:
            return 1
        elif stock_list[mid] < target:
            start = mid +1
        else:
            end = mid -1
    return None



for wish_list_item in wish_list:
    result = binary_search(stock_list, wish_list_item, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')