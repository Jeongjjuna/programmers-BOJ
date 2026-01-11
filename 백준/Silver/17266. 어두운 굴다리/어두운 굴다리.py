import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())  # 굴다리 길이
m = int(input())  # 가로등 개수
arr = list(map(int, input().split()))


def main():
    start, end = 0, 100000
    answer = n
    while start <= end:
        mid = (start + end) // 2

        # mid 의 높이로 모든 길을 밝힐 수 있는가?
        visited = [False] * (n + 1)
        is_posible = True
        for i in range(len(arr)):
            # 시작
            if (i == 0):
                if 0 < arr[i] - mid:
                    is_posible = False
                    break
            # 끝
            if (i == len(arr) - 1):
                if arr[i] + mid < n:
                    is_posible = False
                    break
                if arr[i - 1] + mid < arr[i] - mid:
                    is_posible = False
                    break
            # 중간
            if arr[i - 1] + mid < arr[i] - mid:
                is_posible = False
                break

        if is_posible:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    print(answer)


if __name__ == "__main__":
    main()
