import sys

input = sys.stdin.readline

# 변수 및 입력 선언
a = int(input())
b = int(input())
c = int(input())


def main():
    print(a + b - c)
    print(int(str(a) + str(b)) - c)


if __name__ == "__main__":
    main()
