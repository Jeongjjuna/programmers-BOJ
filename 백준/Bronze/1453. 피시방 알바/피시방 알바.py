import sys

input = sys.stdin.readline

# 변수 및 입력 선언

n = int(input().strip())
seats = list(map(int, input().split()))


def main():
    occupied = [False] * 101
    reject_count = 0

    for s in seats:
        if occupied[s]:
            reject_count += 1
        else:
            occupied[s] = True

    print(reject_count)


if __name__ == "__main__":
    main()
