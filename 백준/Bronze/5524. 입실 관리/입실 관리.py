import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
arr = []
for _ in range(n):
    arr.append(input().strip())


def main():
    for elem in arr:
        print(elem.lower())


if __name__ == "__main__":
    main()
