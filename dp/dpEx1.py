# x = int(input())

# d = [0] * 30001 # dp테이블 초기화
#
# for i in range(2, x+1):
#     d[i] = d[i-1] + 1
#     if i % 2 ==0:
#         d[i] = min(d[i], d[i//2]+1)
#     if i % 3 ==0:
#         d[i] = min(d[i], d[i//3]+1)
#     if i % 5 ==0:
#         d[i] = min(d[i], d[i//5]+1)
#
# print(d[x])

x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1 # -1
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1) # 순차적으로 계산된 d[i]와 d[i//5]+1 중 적은 값 판단.
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

print(d[x])



