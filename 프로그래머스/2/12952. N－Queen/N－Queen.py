import sys

sys.setrecursionlimit(100000)


def check(n, d, visited, row, col):
    for key in d:
        if abs(key[0] - row) == abs(key[1] - col):
            return True
    return False


def n_queen(n, d, visited, row, answer):
    if row == n:
        answer[0] += 1
        return
    
    for col in range(n):
        # 같은 열에 없고
        if not visited[col]:
            # 대각선에도 없다면
            if not check(n, d, visited, row, col):
                visited[col] = True
                d[(row, col)] = 1
                n_queen(n, d, visited, row + 1, answer)
                visited[col] = False
                del d[(row, col)]
                

def solution(n):
    
    d = dict()
    visited = [False] * n
    init_row = 0
    answer = [0]
    
    n_queen(n, d, visited, init_row, answer)
    
    return answer[0]