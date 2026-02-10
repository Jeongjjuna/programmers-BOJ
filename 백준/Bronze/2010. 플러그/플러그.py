import sys

input = sys.stdin.readline

n = int(sys.stdin.readline())


def main():
    total = 0
    for _ in range(n):
        num = int(input())
        total += num

    print(total - (n - 1))


if __name__ == "__main__":
    main()
