from collections import deque, defaultdict


'''
공평하게 자르기 : 조각에 동일한 가짓수의 토핑
'''
def solution(topping):
    return solution_2(topping)


# 접근 1. 완전탐색
def solution_1(topping):
    fair_list = [is_fair(idx, topping) for idx in range(1, len(topping))]
    return sum(fair_list)


# idx를 기준으로 나눴을 때 공평하면 True, 아니면 False
def is_fair(idx, topping):
    # print(topping[0:idx], end = " ")
    # print(topping[idx:])
    return len(set(topping[0:idx])) == len(set(topping[idx:]))


def solution_2(topping):
    
    first = deque(topping[:1])
    first_uniqe = defaultdict(int)
    for elem in first:
        first_uniqe[elem] += 1

    second = deque(topping[1:])
    second_uniqe = defaultdict(int)
    for elem in second:
        second_uniqe[elem] += 1
    
    # answer 초기화
    if len(first_uniqe) == len(second_uniqe):
        answer = 1
    else:
        answer = 0
        
    while len(second) != 0:
        data = second.popleft()
        
        second_uniqe[data] -= 1
        if second_uniqe[data] == 0:
            del second_uniqe[data]
            
        first.append(data)
        first_uniqe[data] += 1
        
        if len(first_uniqe) == len(second_uniqe):
            answer += 1
        
    
    return answer







