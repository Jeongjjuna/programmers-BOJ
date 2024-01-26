def check_ans(pattern, answers):
    n = len(pattern)
    
    cnt, idx = 0, 0
    for answer in answers:
        if answer == pattern[idx]:
            cnt += 1
        idx = (idx + 1) % n
        
    return cnt


def solution(answers):

    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # (사람, 맞춘개수) 사람 = 1, 2, 3
    answer = []
    for i, pattern in enumerate(patterns):
        cnt = check_ans(pattern, answers)
        answer.append((i + 1, cnt))
    
    max_cnt = max([elem[1] for elem in answer])
    return sorted([elem[0] for elem in answer if elem[1] == max_cnt])