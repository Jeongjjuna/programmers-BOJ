from collections import deque

def solution(progresses, speeds):

    # [7, 3, 9]
    deploy_possible_time = deque()
    for p, s in zip(progresses, speeds):
        t = (100 - p)
        if t % s == 0:
            deploy_possible_time.append(t // s)
        else:
            deploy_possible_time.append(t // s + 1)
    
    # print(deploy_possible_time)
    
    
    answer = []
    while True:
        if len(deploy_possible_time) == 0:
            break
            
        k = deploy_possible_time.popleft()
        cnt = 1
        while len(deploy_possible_time) != 0 and deploy_possible_time[0] <= k:
            deploy_possible_time.popleft()
            cnt += 1
        answer.append(cnt)
        
    return answer








