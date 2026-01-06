import sys

input = sys.stdin.readline

# 변수 및 입력 선언
k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))


def main():
    # 오름차순
    arr.sort()

    # 이진탐색으로 자를 수 있는 최대 길이를 구하자. 최대 길이 -> 최대로 많은 개수
    answer = 0
    start, end = 0, 2 ** 31 - 1
    while start <= end:

        mid = (start + end) // 2

        # mid 길이로 전부 나눴을 때 가능한지?
        cnt = 0
        for elem in arr:
            cnt += (elem // mid)

        if n <= cnt:
            # 가능
            start = mid + 1
            answer = max(answer, mid)
        else:
            # 불가능
            end = mid - 1

    print(answer)


if __name__ == "__main__":
    main()
