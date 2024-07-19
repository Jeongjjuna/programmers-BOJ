import sys; input = sys.stdin.readline


# 변수 입력 및 선언
N, M, L, K = map(int, input().split())
arr = []
rows, cols = [], []
for _ in range(K):
    # x = 가로,  y = 세로
    x, y = map(int, input().split())
    arr.append((y, x))
    rows.append(y)
    cols.append(x)

# 최대로 덮을 수 있는 개수
wrap_cnt = 0

for p1 in arr:
    for p2 in arr:
        # 우측 하단
        cnt = 0
        for tx, ty in arr: # O(100)
            if p1[0] <= tx <= p1[0] + L and p2[1] <= ty <= p2[1] + L:
                cnt += 1
        wrap_cnt = max(wrap_cnt, cnt)

print(K - wrap_cnt)