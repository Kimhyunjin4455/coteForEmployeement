#1
# n,m,k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n-1]
# second = data[n-2]
#
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
#
# print(result)

#2
# n,m,k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n-1]
# second = data[n-2]
#
# # 가장 큰수가 더해지는 횟수(사용 횟수)
# cnt = int(m/(k+1)) * k
# cnt += m % (k+1)
#
# result = 0
# result += (cnt) * first
# result += (m-cnt) * second
#
# print(result)
#


#Re resolve
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_idx = data[n-1]
second_idx = data[n-2]

result = 0

# m회 더하면서 결과값을 올리고 그 횟수만큼 m이 0이 될때까지 차감하는 방식
while True:
    if m==0:
        break
    for i in range(k):
        result += first_idx
        m -=1
    result += second_idx
    m-=1

print(result)

