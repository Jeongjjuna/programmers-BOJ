from collections import deque

# 올바른 괄호문자열이면 return 1
# 그렇지 않으면 return 0
def is_correct(x):
    stack = []
    
    for elem in x:
        if not stack:
            stack.append(elem)
            continue
            
        if elem in ['[', '(', '{']:
            stack.append(elem)
            continue
        
        if stack[-1] == '[' and elem == ']':
            stack.pop()
        elif stack[-1] == '(' and elem == ')':
            stack.pop()
        elif stack[-1] == '{' and elem == '}':
            stack.pop()
    
    if not stack:
        return 1
    else:
        return 0
    
    
def solution(s):
    
    sq = deque(list(s))
    n = len(s)
    
    # 총 x번 회전시킴
    ans = 0
    for _ in range(n): # O(1000)
        ans += is_correct(sq)
        sq.append(sq.popleft())
        
    return ans