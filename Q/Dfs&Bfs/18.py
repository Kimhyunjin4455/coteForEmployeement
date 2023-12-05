# 균형잡힌 괄호 문자열 (원래의 문자열을 분리하기 위해 인덱스를 알아야 함)

# 올바른 괄호 문자열 (이 함수의 참/거짓여부를 통해 다음 진행을 결정)

def balanced_sentence(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return i

def collect_sentence(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True



def solution(p):
    answer = ''

    if answer == '':
        return answer

    index = balanced_sentence(p)

    u = p[:index+1]
    v = p[index+1:]

    # 균형 잡힌 괄호 문자열 판별하는 함수로 인덱스를 구해 두 문자열로 분리

    # u에 대해 올바른 괄호 문자열인지 판별, 그 후 과정 수행

    if collect_sentence(u):
        answer = u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'

        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)

    # 올바르지 않다면 '(' ')'을 수행한 문자열의 양끝에 이어 붙임

    # 첫번째와 마지막 문자를 제거하고 방향 반대로
    return answer


