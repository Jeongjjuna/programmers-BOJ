from collections import deque
import sys; input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    dq = deque()
    for idx, elem in enumerate(arr):
        if idx % 2 == 0:
            dq.append(elem)
        else:
            dq.appendleft(elem)
    
    # 최소 난이도 찾기
    ans = abs(dq[0] - dq[-1])
    for i in range(len(dq) - 1):
        ans = max(ans, abs(dq[i] - dq[i + 1]))

    print(ans)