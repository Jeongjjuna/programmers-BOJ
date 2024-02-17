def is_correct(s):
    stack = []
    for x in s:
        if len(stack) == 0:
            stack.append(x)
            continue

        if stack[-1] == '(' and x == ')':
            stack.pop()
        else:
            stack.append(x)

    if len(stack) == 0:
        return True
    else:
        return False

    
def separate(w):
    cnt = [0, 0]
    for x in w:
        if x == ')':
            cnt[0] += 1
        elif x == '(':
            cnt[1] += 1

        if cnt[0] == cnt[1]:
            break
    
    # 인덱스 위치
    idx = cnt[0]
    u = w[:2*idx]
    v = w[2*idx:]
    return u, v


def dfs(w):
    # 1. 빈 문자열을 경우
    if w == "":
        return ""
    
    # 두개의 올바른 괄호 문자열로 분리한다.
    u, v = separate(w)
    
    if is_correct(u):
        return u + dfs(v)
    else:
        f = '(' + dfs(v) + ')'
        k = ''
        for x in u[1:-1]:
            if x == ')':
                k += '('
            else:
                k += ')'
        return f + k
     

def solution(w):
    return dfs(w)