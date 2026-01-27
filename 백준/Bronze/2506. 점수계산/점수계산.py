import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
arr = list(map(int, input().split()))


def main():
    for i in range(1, n):
        if arr[i] == 0:
            continue

        if arr[i - 1] != 0:
            arr[i] = arr[i - 1] + 1

    print(sum(arr))


if __name__ == "__main__":
    main()
