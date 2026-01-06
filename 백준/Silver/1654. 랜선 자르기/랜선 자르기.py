import sys; input = sys.stdin.readline


if __name__ == "__main__":
    k, n = map(int, input().split())
    arr = [int(input()) for _ in range(k)]

    # 이진탐색을 진행합니다.
    left, right = 1, max(arr)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        
        # mid로 잘랐을 때 나오는 개수
        cnt = 0
        for elem in arr:
            cnt += elem // mid

        if cnt >= n:
            ans = max(ans, mid)
            left = mid + 1  
        else:
            right = mid - 1

    print(ans)