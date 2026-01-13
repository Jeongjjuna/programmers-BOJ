import sys

input = sys.stdin.readline

# 변수 및 입력 선언
size = 5
arr = []
for _ in range(size):
    arr.append(int(input()))


def main():
    # 평균
    avg = sum(arr) // size

    # 중앙값
    arr.sort()
    mid = arr[2]

    print(avg)
    print(mid)


if __name__ == "__main__":
    main()
