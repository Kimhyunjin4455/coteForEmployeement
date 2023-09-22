n = int(input())
array = [0] * 1000001

for i in input().split(): # 가게에 있는 전체 부품 번호를 입력받아서 기록
    array[int(i)] = 1

m = int(input())
wishlist = list(map(int, input().split()))

for i in wishlist:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')