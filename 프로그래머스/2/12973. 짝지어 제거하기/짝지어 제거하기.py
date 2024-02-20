def solution(s):
    stack = []
    
    for elem in s:
        
        if len(stack) == 0:
            stack.append(elem)
            continue
            
        if stack[-1] == elem:
            stack.pop()
        else:
            stack.append(elem)
            
    if len(stack) == 0:
        return 1
    else:
        return 0
        