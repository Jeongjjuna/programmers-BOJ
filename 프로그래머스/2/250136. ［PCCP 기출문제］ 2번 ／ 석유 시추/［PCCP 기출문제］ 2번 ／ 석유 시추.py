from collections import deque

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

def is_range(x, y, land):
    return 0 <= x < len(land) and 0 <= y < len(land[0])


def bfs(x, y, land, visited, no):

    cnt = 0
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt += 1
    land[x][y] = no
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny, land):
                if not visited[nx][ny]:
                    if land[nx][ny] == 1:
                        visited[nx][ny] = True
                        cnt += 1
                        land[nx][ny] = no
                        q.append((nx, ny))
                        
    return cnt

def solution(land):
    # 1석유
    # [[0, 0, 0, 1, 1, 1, 0, 0],
    # [0, 0, 0, 0, 1, 1, 0, 0],
    # [1, 1, 0, 0, 0, 1, 1, 0],
    # [1, 1, 1, 0, 0, 0, 0, 0],
    # [1, 1, 1, 0, 0, 0, 1, 1]
    
    # 각 석유 영영에 고유 번호를 붙인다.
    # 고유 번호의 석유 개수를 구한다.
    
    
    no = 2 # 고유 번호
    row, col = len(land), len(land[0])
    visited = [[False]*col for _ in range(row)]
    d = dict()
    for x in range(row):
        for y in range(col):
            if land[x][y] == 0:
                continue
            
            if not visited[x][y] and land[x][y] == 1:
                cnt = bfs(x, y, land, visited, no)
                d[no] = cnt
                no += 1
                
                
    # [[0, 0, 0, 2, 2, 2, 0, 0],
    # [0, 0, 0, 0, 2, 2, 0, 0],
    # [3, 3, 0, 0, 0, 2, 2, 0],
    # [3, 3, 3, 0, 0, 0, 0, 0],
    # [3, 3, 3, 0, 0, 0, 4, 4]]
    
    # d = {2: 7, 3: 8, 4: 2}
    
    ans = 0
    for y in range(col):
        s = set()
        for x in range(row):
            if (land[x][y] == 0):
                continue
            s.add(land[x][y])
        
        count = 0
        for elem in list(s):
            count += d[elem]
        
        ans = max(ans, count)
    
    return ans