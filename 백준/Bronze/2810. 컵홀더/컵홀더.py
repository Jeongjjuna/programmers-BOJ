import sys

input = sys.stdin.readline


def main():
    n = int(input())
    seat = input()

    # 커플석 개수
    couple = seat.count("LL")

    # 컵홀더 개수 = n + 1 - couple
    cup_holder = n + 1 - couple

    # 컵을 꽂을 수 있는 최대 인원
    print(min(n, cup_holder))


if __name__ == "__main__":
    main()
