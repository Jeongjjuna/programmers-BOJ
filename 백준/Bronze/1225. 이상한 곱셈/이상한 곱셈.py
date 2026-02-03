import sys

input = sys.stdin.readline

# 변수 및 입력 선언
a, b = input().split()


def main():
    sum_a = sum(int(x) for x in a)
    sum_b = sum(int(x) for x in b)

    print(sum_a * sum_b)


if __name__ == "__main__":
    main()
