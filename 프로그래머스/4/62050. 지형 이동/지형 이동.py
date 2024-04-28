import sys; sys.setrecursionlimit(1000000)

def solution(land, height):
    
    # 사다리 설치 비용의 최솟값
    
    
    # 아이디어1.
    # 덩어리를 구한다.(dfs)
    # 모든 덩어리를 잇는 사다리 최소값
    
    idx = 1
    n = len(land)
    visited = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = idx
                dfs(land, visited, height, i, j, idx)
                idx += 1
    
    
    # visited를 토대로 서로 다른 땅 사이간에 간선 정보 생성
    edges = []
    for i in range(n):
        for j in range(n):
            
            for dx, dy in zip([0, 1], [1, 0]):
                nx, ny = i + dx, j + dy
                if not is_range(land, nx, ny):
                    continue

                if visited[i][j] != visited[nx][ny]:
                    w = abs(land[i][j] - land[nx][ny])
                    edges.append((visited[i][j], visited[nx][ny], w))
    
    
    # 크루스컬 알고리즘 적용
    edges.sort(key = lambda x : x[2])
    uf = list(range(idx))
    
    min_weight = 0
    for a, b, w in edges:
        if find(a, uf) != find(b, uf):
            union(a, b, uf)
            min_weight += w

    return min_weight


def union(x, y, uf):
    X, Y = find(x, uf), find(y, uf)
    uf[X] = Y

def find(x, uf):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x], uf)
    return uf[x]


def dfs(land, visited, height, x, y, idx):
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(land, visited, height, x, y, nx, ny):
            visited[nx][ny] = idx
            dfs(land, visited, height, nx, ny, idx)


def can_go(land, visited, height, x, y, nx, ny):
    if is_range(land, nx, ny):
        if not visited[nx][ny]:
            if abs(land[x][y] - land[nx][ny]) <= height:
                return True
    return False
                    
    
def is_range(land, nx, ny):
    n = len(land)
    return 0 <= nx < n and 0 <= ny < n