import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))


def main():
    # 이진 탐색을 위한 정렬
    arr.sort()

    answer = 0
    start, end = 0, sys.maxsize
    while (start <= end):

        # 나눠줄 용량
        mid = (start + end) // 2

        # 총 k명에게 나눠줄 수 있는지 계산
        count = 0
        for elem in arr:
            # 막걸리는 용량이 0일 수 있음. >> 예외처리
            if mid == 0:
                continue

            count += (elem // mid)  # 개수

        if m <= count:
            # 가능
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1

    print(answer)


if __name__ == "__main__":
    main()
