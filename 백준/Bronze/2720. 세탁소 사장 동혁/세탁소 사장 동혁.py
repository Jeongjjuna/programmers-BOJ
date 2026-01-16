import sys

input = sys.stdin.readline

# 변수 및 입력 선언
t = int(input())
pay = [25, 10, 5, 1]


def main():
    for _ in range(t):
        money = int(input())

        answer = []
        for elem in pay:
            mod = money // elem
            answer.append(mod)
            money %= elem

        print(*answer)


if __name__ == "__main__":
    main()
