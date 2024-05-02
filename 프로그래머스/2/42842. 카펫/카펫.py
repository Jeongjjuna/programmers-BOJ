# 8, 2000000 = 2000008 -> [2809,712]
# 5000, 1 =  5001 -> [1667,3]
# 5000, 2000000 = 2005000 -> [1604,1250]

def solution(brown, yellow):
    
    answer = []
    
    # 전체 블록의 개수
    s = brown + yellow    
    
    # 곱해서 s가 나오는 경우의 수
    
    for i in range(3, s + 1): # 세로 길이
        for j in range(i, int(s/i) + 1): # 가로 길이
            if i * j == s:
                
                if brown == (j*2 + i*2 - 4):
                
                    answer = [j, i]

    
    return answer