import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n, m = map(int, input().split())

def main():
    answer = abs(n - m)
    print(answer)


if __name__ == "__main__":
    main()
