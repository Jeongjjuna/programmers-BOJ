import math
import sys

input = sys.stdin.readline

# 변수 및 입력 선언
D, H, W = map(int, input().split())


def main():
    ratio = D / math.sqrt(H ** 2 + W ** 2)

    height = int(H * ratio)
    width = int(W * ratio)

    print(height, width)


if __name__ == "__main__":
    main()
