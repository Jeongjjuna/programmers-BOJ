import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())  # 지방의 수
arr = list(map(int, input().split()))  # 지방 예산 요청
m = int(input())  # 총 예산수


def main():
    # 오름차순
    arr.sort()

    answer = 0
    start, end = 0, max(arr)
    while start <= end:
        mid = (start + end) // 2

        sum = 0
        for elem in arr:
            sum += min(mid, elem)

        if sum <= m:
            # 가능
            answer = max(answer, mid)
            start = mid + 1
        else:
            # 불가능
            end = mid - 1

    print(answer)


if __name__ == "__main__":
    main()
