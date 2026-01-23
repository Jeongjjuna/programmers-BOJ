import sys

input = sys.stdin.readline

# 변수 및 입력 선언
T = int(input())


def main():
    for _ in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())

        count = 0
        for _ in range(n):
            cx, cy, r = map(int, input().split())

            # 출발점이 원 내부인지 확인
            inside1 = (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2
            # 도착점이 원 내부인지 확인
            inside2 = (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2

            # 하나만 내부라면 진입/탈출 필요
            if inside1 != inside2:
                count += 1

        print(count)


if __name__ == "__main__":
    main()
