import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
arr = []
for _ in range(n):
    arr.append(input().strip())


def main():
    arr_unique = list(set(arr))
    arr_unique.sort(key=lambda x: (len(x), x))
    for elem in arr_unique:
        print(elem)


if __name__ == "__main__":
    main()
