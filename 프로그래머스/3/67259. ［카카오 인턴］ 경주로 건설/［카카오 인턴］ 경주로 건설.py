import heapq
import sys


INF = sys.maxsize


def is_range(x, y, n):
    return 0 <= x < n and 0 <= y < n


def can_go(nx, ny, board):
    if is_range(nx, ny, len(board)):
        if board[nx][ny] == 0:
            return True
    return False


def solution(board):
    
    '''
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
    '''
    n = len(board)
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    distance = [[[INF]*4 for _ in range(n)] for _ in range(n)] # 비용을 담는다.
    
    q = []
    start_x, start_y = 0, 0
    
    # (최소거리, x, y, 방향)
    heapq.heappush(q, (0, start_x, start_y, 1)) # 동쪽출발
    distance[start_x][start_y][1] = 0
    heapq.heappush(q, (0, start_x, start_y, 2)) # 남쪽출발
    distance[start_x][start_y][2] = 0
    
    while q:
        dist, x, y, dire = heapq.heappop(q)
        # print(dist, x, y, dire)
        
        # 다익스트라 조건
        if distance[x][y][dire] != dist:
            continue
        
        for i in range(4):
            # 왔던 길은 돌아가지 않음
            if abs(i - dire) == 2:
                continue
                
            dx, dy = dxs[i], dys[i]
            nx, ny = x + dx, y + dy
            
            # 직선 비용 계산
            cost = dist + 100
            # 만약 코너라면 코너 비용추가
            if dire != i: 
                cost = cost + 500
                
            if can_go(nx, ny, board):
                if cost < distance[nx][ny][i]:
                    distance[nx][ny][i] = cost
                    heapq.heappush(q, (cost, nx, ny, i))
                    
                    
    '''
    [0, 100, INF, 2000]
    [100, 700, 1300, 1400]
    [200, INF, 1900, INF]
    [INF, 2600, 2000, 2600]
    '''
    
    '''
    [0, 100, INF, 2000],
    [100, 700, 1300, 1400],
    [200, INF, 1900, INF],
    [INF, 2600, 2000, 2600]
    '''
    
    return min(distance[n - 1][n - 1])