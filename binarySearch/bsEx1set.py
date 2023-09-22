n = int(input())
stocklist = set(map(int, input().split()))

m = int(input())
wishlist = list(map(int, input().split()))

for i in wishlist:
    if i in stocklist:
        print('yes', end=' ')
    else:
        print('no', end=' ')