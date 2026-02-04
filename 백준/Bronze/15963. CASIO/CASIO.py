import sys

input = sys.stdin.readline

# 변수 및 입력 선언
a, b = input().split()


def main():
    if a == b:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
