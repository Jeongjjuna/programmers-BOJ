import sys; input = sys.stdin.readline
from collections import deque

def bfs(arr, start):
    q = deque()
    q.append(start)
    visited = [False] * n

    while q:
        v = q.popleft()

        for nv, val in enumerate(arr[v]):
            if val == 1 and not visited[nv]:
                visited[nv] = True
                q.append(nv)

    return visited


# 변수 입력 및 선언
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = [[0] * n for _ in range(n)]


# 모든 노드에 대해 bfs 탐색한다.
for v in range(n):
    visited = bfs(arr, v)

    for i in range(n):
        if visited[i]:
            answer[v][i] = 1


# 출력
for elem in answer:
    print(*elem)