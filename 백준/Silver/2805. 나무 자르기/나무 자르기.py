import bisect
import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n, m = map(int, input().split())
arr = list(map(int, input().split()))


def main():
    arr.sort()

    start, end = 0, max(arr)
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        # mid 보다 큰 나무들의 시작 인덱스
        index = bisect.bisect_right(arr, mid)

        # 잘려서 얻는 나무 길이
        wood = sum(arr[index:]) - mid * (n - index)

        if wood >= m:
            answer = mid  # 가능한 높이 저장
            start = mid + 1  # 더 높게 시도
        else:
            end = mid - 1  # 낮춰야 함

    print(answer)


if __name__ == "__main__":
    main()
