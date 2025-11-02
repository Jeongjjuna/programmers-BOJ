import sys
from collections import deque

readline = sys.stdin.readline

# a -> b 로 옮길 수 있는 물의 양을 리턴
def get_water(a, capacity_a, b, capacity_b):
    # a통에 물이 없거나, b통이 이미 꽉 찼으면 이동 불가
    if a == 0 or b == capacity_b:
        return None

    # 실제로 옮길 수 있는 양
    return min(a, capacity_b - b)


def is_range(a, b, c):
    return 0 <= a <= MAX and 0 <= b <= MAX and 0 <= c <= MAX

def bfs(visited, A, B, C):
    answer = set()
    queue = deque()
    visited[0][0][C] = True
    queue.append((0, 0, C))
    while queue:
        a, b, c = queue.popleft()

        if a == 0:
            answer.add(c)

        # a -> b
        water = get_water(a, A, b, B)
        if water is not None:
            na, nb, nc = a - water, b + water, c
            if is_range(na, nb, nc) and not visited[na][nb][nc]:
                visited[na][nb][nc] = True
                queue.append((na, nb, nc))

        # a -> c
        water = get_water(a, A, c, C)
        if water is not None:
            na, nb, nc = a - water, b, c + water
            if is_range(na, nb, nc) and not visited[na][nb][nc]:
                visited[na][nb][nc] = True
                queue.append((na, nb, nc))

        # b -> a
        water = get_water(b, B, a, A)
        if water is not None:
            na, nb, nc = a + water, b - water, c
            if is_range(na, nb, nc) and  visited[na][nb][nc]:
                visited[na][nb][nc] = True
                queue.append((na, nb, nc))

        # b -> c
        water = get_water(b, B, c, C)
        if water is not None:
            na, nb, nc = a, b - water, c + water
            if is_range(na, nb, nc) and not visited[na][nb][nc]:
                visited[na][nb][nc] = True
                queue.append((na, nb, nc))

        # c -> a
        water = get_water(c, C, a, A)
        if water is not None:
            na, nb, nc = a + water, b, c - water
            if is_range(na, nb, nc) and not visited[na][nb][nc]:
                visited[na][nb][nc] = True
                queue.append((na, nb, nc))

        # c -> b
        water = get_water(c, C, b, B)
        if water is not None:
            na, nb, nc = a, b + water, c - water
            if is_range(na, nb, nc) and  visited[na][nb][nc]:
                visited[na][nb][nc] = True
                queue.append((na, nb, nc))

    return answer


def solution(A, B, C):
    visited = [[[False] * (MAX + 1) for _ in range(MAX + 1)] for _ in range(MAX + 1)]

    answer_set = bfs(visited, A, B, C) # set
    answers = (list(answer_set))
    answers.sort()
    print(* answers)

if __name__ == '__main__':
    MAX = 200
    A, B, C = map(int, readline().split())
    solution(A, B, C)