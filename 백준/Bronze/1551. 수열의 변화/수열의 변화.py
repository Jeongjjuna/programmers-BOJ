import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n, k = map(int, input().split())
arr = list(map(int, input().strip().split(',')))


def main():
    global arr

    for _ in range(k):
        new_arr = []
        for i in range(len(arr) - 1):
            new_arr.append(arr[i + 1] - arr[i])

        arr = new_arr

    # 출력 (콤마로 구분)
    print(','.join(map(str, arr)))


if __name__ == "__main__":
    main()
