from collections import defaultdict

def solution(id_list, report, k):

    # a가 신고한 사람들 {a : set(b, c, d)}
    log = defaultdict(set)
    
    # a가 신고당한 횟수 {a : 2, b : 1}
    count = defaultdict(int)

    
    for r in report:        
        # a가 b를 신고했다.
        a, b = r.split()

        if b not in log[a]:
            count[b] += 1
            log[a].add(b)
            
    
    
    result = []
    
    for user_id in id_list:
        # user_id가 신고한 set구조
        cnt = 0
        for reported_id in log[user_id]:
            if count[reported_id] >= k:
                cnt += 1
        result.append(cnt)

    return result