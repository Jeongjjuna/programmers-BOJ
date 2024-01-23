import sys; input = sys.stdin.readline


# 접근 -> 우선순위 정렬
# 절대값이 가장 큰쪽이 마지막 값이 된다.
if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    left, right = [], []
    max_abs = 0
    for elem in arr:
        if elem < 0:
            left.append(elem)
        else:
            right.append(elem)
        max_abs = max(max_abs, abs(elem))
        

    left.sort()
    right.sort()

    ans = 0

    # 왼쪽계산 [-39, -37, -29, -28, -6] 
    for i in range(0, len(left), m):
        ans += abs(left[i]*2)

    # 오른쪽계산 [2, 11]
    for i in range(len(right) - 1, -1, -m):
        ans += right[i]*2

    
    print(ans - max_abs)