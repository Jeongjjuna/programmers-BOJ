def count_answer(p, patterns, answers):
    # p사용자의 패턴 : [1, 2, 3, 4, 5]
    pattern = patterns[p - 1] 
    n = len(pattern)
    
    cnt, idx = 0, 0
    for answer in answers:
        no = (idx % n)
        if pattern[no] == answer:
            cnt += 1
        idx += 1
        
    return cnt
    

def solution(answers):
    
    # 찍는 방식 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # {사람 : 맞은개수}
    score = dict()
    
    # 1 ~ 3 번 사람의 맞은 개수를 구한다.
    for p in range(1, 4):
        cnt = count_answer(p, patterns, answers)
        score[p] = cnt
        
    # score 가장 큰 값 찾기
    max_cnt = 0
    for x in score.values():
        max_cnt = max(max_cnt, x)
    
    # 가장큰값 max_cnt와 같은 점수인 사람들 찾기
    ans = []
    for x in score.keys():
        if score[x] == max_cnt:
            ans.append(x)
    
    return sorted(ans)