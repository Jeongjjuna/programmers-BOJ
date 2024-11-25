import sys; input = sys.stdin.readline


# 풀이
t = int(input())
for _ in range(t):
    # l = 막대의 길이, n = 개미의 수
    l, n = map(int, input().split())

    point = []
    for _ in range(n):
        point.append(int(input()))


    # 개미 방향 전환을 고려하지 않아도 된다..?
    
    point.sort()

    # 최대 시간 구하기
    max_time = max(point[-1], l - point[0])

    # 최소 시간 구하기
    min_time = min(point[0], l - point[0])
    for p in point:
        # 가야할 방향 최소길
        time = min(l - p, p)
        min_time = max(min_time, time)

    print(min_time, max_time)