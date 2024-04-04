from collections import deque
import sys


def bfs(start, visited, arr):
    cnt = 1
    q = deque()
    q.append(start)
    
    while q:
        cnt += 1
        v = q.popleft()
        
        for nv in arr[v]:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)
    
    return cnt


# 접근 1. 완전탐색
def sol_1(n, wires):
    
    # 인접 리스트 만들기
    arr = [[] for _ in range(n + 1)]
    for wire in wires:
        node_1, node_2 = wire[0], wire[1]
        arr[node_1].append(node_2)
        arr[node_2].append(node_1)
    
    answer = sys.maxsize
    for wire in wires:
        node_1, node_2 = wire[0], wire[1]
        
        # 두 간선 끝점을 방문처리한다
        visited = [None] + [False] * n
        visited[node_1] = True
        visited[node_2] = True
        
        # 두 전력망 개수의 차이 최소값 구하기
        cnt_1 = bfs(node_1, visited, arr)
        cnt_2 = bfs(node_2, visited, arr)
        answer = min(answer, abs(cnt_1 - cnt_2))
        
    return answer


def solution(n, wires):    
    return sol_1(n, wires)