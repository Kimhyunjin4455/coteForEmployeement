#풀이(입력 예시 통과)
# n,k = map(int, input().split())
# cnt = 0
# while n != 1:
#     if n%k ==0:
#         n /= k
#         cnt +=1
#     else:
#         n -= 1
#         cnt +=1
# print(cnt)

#1
# n,k = map(int, input().split())
# result = 0
#
# while n>=k:
#     while n % k != 0:
#         n -=1
#         result +=1
#     n //=k
#     result +=1
#
# while n>1:
#     n-=1
#     result +=1
#
# print(result)

#2
# n,k = map(int, input().split())
# result_2 = 0
#
# while True:
#     # (n == k로 나누어 떨어지는 수)가 될때까지 1 빼기
#     target = (n//k) *k
#     result_2 += (n-target)
#     n = target
#     # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복 종료됨
#     if n <k:
#         break
#     result_2 +=1
#     n //=k
#
# # 마지막으로 남은 수에 대해 1씩 빼기
# result_2 += (n-1)
# print(result_2)

# Re resolve
n, m = map(int, input().split())
cnt = 0

while n !=1:

    if n % m == 0:
        n //= m
        cnt += 1
    else:
        n -=1
        cnt +=1
print(cnt)


