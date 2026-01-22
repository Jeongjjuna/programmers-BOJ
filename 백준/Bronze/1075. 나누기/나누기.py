import sys

input = sys.stdin.readline

# 변수 및 입력 선언
N = int(input())
F = int(input())


def main():
    base = (N // 100) * 100

    for i in range(100):
        if (base + i) % F == 0:
            # i를 두 자리 형식으로 출력
            print(f"{i:02d}")
            break


if __name__ == "__main__":
    main()
