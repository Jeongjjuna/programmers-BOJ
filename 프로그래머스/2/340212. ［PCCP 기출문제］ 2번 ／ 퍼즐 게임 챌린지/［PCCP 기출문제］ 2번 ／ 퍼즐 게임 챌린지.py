import sys; sys.setrecursionlimit(1000000)

INF = sys.maxsize
ans = INF

def is_possible(diffs, times, limit, level): # -> bool
    # 현재 level로 모든 퍼즐을 해결 가능?
    
    diff_len = len(diffs)
    total_time = 0
    
    for idx in range(diff_len):
        diff = diffs[idx]
        time = times[idx]
        
        if (diff <= level):
            total_time += time
        else:
            false_count = diff - level # 틀린 횟수
            
            if idx == 0:
                plus = 1
            else:
                plus = times[idx - 1]
            total_time += (time + plus) * false_count + time
            
    return total_time <= limit
    

def binary_search(start, end, diffs, times, limit):
    global ans
    
    if (start > end):
        return
    
    mid = (start + end) // 2
    
    # level이 mid일 때, 제한 시간 내에 퍼즐을 모두 해결할 수 있는가?
    result = is_possible(diffs, times, limit, mid)
    
    if result:
        ans = min(ans, mid)
        binary_search(start, mid - 1, diffs, times, limit)
    else:
        binary_search(mid + 1, end, diffs, times, limit)

def solution(diffs, times, limit):
    global ans
    # 난이도[1, 5, 3]	소요시간[2, 4, 7]	30	3
    
    
    # start ~ end 범위에서 최속값 이진탐색
    start, end = 1, 100000
    binary_search(start, end, diffs, times, limit)
    
    return ans


assert is_possible([1, 5, 3], [2, 4, 7], 30, 4) == True
assert is_possible([1, 5, 3], [2, 4, 7], 30, 3) == True
assert is_possible([1, 5, 3], [2, 4, 7], 30, 2) == False
assert is_possible([1, 5, 3], [2, 4, 7], 30, 1) == False