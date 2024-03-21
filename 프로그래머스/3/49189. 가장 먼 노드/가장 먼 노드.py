from collections import deque

def solution(n, edge):
    
    # 인접리스트 만들기
    arr = [None] + [[] for _ in range(n)]
    for elem in edge:
        a, b = elem[0], elem[1]
        arr[a].append(b)
        arr[b].append(a)

    # bfs로 거리 기록하기
    q = deque()
    visited = [None] + [False] * n
    dist = [None] + [0] * n
    
    start_node = 1
    q.append(start_node)
    visited[start_node] = True
    
    # BFS 탐색
    while q:
        x = q.popleft()
        
        for nx in arr[x]:
            if not visited[nx]:
                visited[nx] = True
                dist[nx] = dist[x] + 1
                q.append(nx)
    

    max_dist = max(dist[1:])
    ans = 0
    for i in range(1, n + 1):
        if dist[i] == max_dist:
            ans += 1

    return ans



