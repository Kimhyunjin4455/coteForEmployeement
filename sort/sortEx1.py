n = int(input())
answer = []
for _ in range(n):
    answer.append(int(input()))
    
# answer.sort(reverse=True)
# for i in range(len(answer)):
#     print(answer[i], end=' ')

answer = sorted(answer, reverse=True)
for i in answer:
    print(i, end=' ')