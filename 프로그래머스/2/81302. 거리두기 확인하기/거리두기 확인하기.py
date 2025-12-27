from collections import deque

size = 5
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < size and 0 <= y and y < size

def can_go(grid, visited, x, y):
    if in_range(x, y) and visited[x][y] == 0:
        if grid[x][y] == "P" or grid[x][y] == "O":
            return True
    return False

def bfs(grid, x, y):
    visited = [[0] * size for _ in range(size)]
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        if visited[x][y] >= 2:
            continue
            
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(grid, visited, nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
    return visited
        

# (x, y) 위치에서 맨하튼 거리 2이내로 앉아있다면 True, 하나라도 만족하지 않으면 False
def check(grid, x, y):
    visited = bfs(grid, x, y)
    visited[x][y] = 0
    for i in range(size):
        for j in range(size):
            if visited[i][j] == 1 or visited[i][j] == 2:
                if grid[i][j] == "P":
                    return False
    return True
                

def validate(place):
    # 1. 2차월 배열로 변환
    grid = [list(row) for row in place]

    # 2. 탐색
    for i in range(size):
        for j in range(size):
            if grid[i][j] == "P":
                checked = check(grid, i, j)
                if not checked:
                    return False
                
    return True
    
    
# 완탐 구현 가능
def solution(places):
    
    answer = []
    for place in places:
        is_valid = validate(place)
        
        if is_valid:
            answer.append(1)
            continue
        answer.append(0)
    
    return answer


assert validate(["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]) == True

