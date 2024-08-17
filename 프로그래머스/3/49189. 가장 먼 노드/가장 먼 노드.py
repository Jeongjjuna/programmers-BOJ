from collections import deque


def bfs(n, start, graph):
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        v = q.popleft()
        
        for nv in graph[v]:
            if not visited[nv]:
                distance[nv] = distance[v] + 1
                visited[nv] = True
                q.append(nv)
    return distance


def find_max_dist(distance):
    return max(distance)    


def solution(n, edge):

    # 인접 리스트 만들기
    graph = [None] + [[] for _ in range(n)]
    for e in edge:
        a, b = e[0], e[1]
        graph[a].append(b)
        graph[b].append(a)
        
    
    # bfs를 수행해서 방문 배열 기록하기
    distance = bfs(n, 1, graph)
    
    # 최대 거리 찾기
    max_dist = find_max_dist(distance)
    
    # 최대 거리를 가지는 노드의 개수 찾기
    answer = 0
    for i in range(1, n + 1):
        if distance[i] == max_dist:
            answer += 1

    return answer

