import sys

input = sys.stdin.readline

# 변수 및 입력 선언
t = int(input().strip())


def main():
    for _ in range(t):
        p, s = input().split()
        p = int(p)
        # 문자열에서 p번째 문자 제거
        result = s[:p - 1] + s[p:]
        print(result)


if __name__ == "__main__":
    main()
