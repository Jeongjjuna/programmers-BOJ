def solution(n, words):
    
    
    start_word = words[0]
    d = dict()
    d[start_word] = True
    answer = [0, 0]
    
    for idx in range(1, len(words)):
        # 끝과 시작이 다르다면
        if start_word[-1] != words[idx][0]:
            # 9 -> [3명중 3번재 사람, 총 3번째]
            m = (idx + 1) % n
            if m == 0:
                answer = [n, (idx + 1)//n]
            else:
                answer = [m, (idx + 1)//n + 1]
            break
    
        # 만약 이전에 말한 단어라면
        if words[idx] in d:
            # 5 -> [2명중 1번째사람, 총 3번째]
            m = (idx + 1) % n
            if m == 0:
                answer = [n, (idx + 1)//n]
            else:
                answer = [m, (idx + 1)//n + 1]
            break
        
        # 이미 말한 단어 체크하기
        d[words[idx]] = True
        start_word = words[idx]
        
    return answer