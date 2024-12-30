import sys; input = sys.stdin.readline

def can_go(arr, mid, m):
    s = 0
    for elem in arr:
        if elem < mid:
            s += elem
        else:
            s += mid

    if s <= m:
        return True
    return False

def binary_search(arr, m, start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        # 상한액 배정으로 가능하다면
        if can_go(arr, mid, m):
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1

    return answer

def main(n, arr, m):
    # 모든 요청이 배정될 수 있는 경우 배정한다.
    if sum(arr) <= m:
        print(max(arr))
        return

    # 특정한 정수 상한액을 정한다.
    mid = max(arr)
    arr.sort()
    result = binary_search(arr, m, 0, mid)
    print(result)


# 변수 입력 및 선언
n = int(input()) # 3 <= <= 10,000
arr = list(map(int, input().split()))
m = int(input()) # n <= <= 1,000,000,000

main(n, arr, m)