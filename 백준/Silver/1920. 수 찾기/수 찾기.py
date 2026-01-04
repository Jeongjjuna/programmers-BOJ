import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

# 방법1. hash
def main():
    exist = dict()
    for elem in arr:  # O(100000)
        exist[elem] = True

    for target in targets:  # O(100000)
        # arr 에 target 이 있는지.
        if (target in exist):
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
