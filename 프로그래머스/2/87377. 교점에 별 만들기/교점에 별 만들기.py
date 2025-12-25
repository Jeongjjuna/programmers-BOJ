def fineMatchDots(a1, b1, c1, a2, b2, c2):
    D = a1 * b2 - a2 * b1
    if D == 0:
        return None  # 평행 or 일치

    x_num = b1 * c2 - b2 * c1
    y_num = a2 * c1 - a1 * c2

    # 정수 교점만 필요한 경우
    if x_num % D != 0 or y_num % D != 0:
        return None

    x = x_num // D
    y = y_num // D

    return (x, y)
    

def solution(line):
    x_max = y_max = -float('inf')
    x_min = y_min = float('inf')
    matched = set()
    
    for i in range(len(line)):
        a, b, c = line[i]
        for j in range(len(line)):
            if (i == j): 
                continue
            
            a2, b2, c2 = line[j]
            
            # 두 직선이 만나는 정수 좌표 구하기
            is_matched = fineMatchDots(a, b, c, a2, b2, c2)
            if (is_matched is not None):
                x, y = is_matched[0], is_matched[1]
                matched.add((x, y))
                x_max, y_max = max(x_max, x), max(y_max, y)
                x_min, y_min = min(x_min, x), min(y_min, y)
    
    width = x_max - x_min + 1
    height = y_max - y_min + 1
    answer = [["."] * width for _ in range(height)]
    
    for (x, y) in matched:
        row = y_max - y
        col = x - x_min
        answer[row][col] = "*"
        
    return list(map(''.join, answer))

assert fineMatchDots(2, -1, 4, -2, -1, 4) == (0, 4)
assert fineMatchDots(1, 0, -1, 1, 0, 1) == None