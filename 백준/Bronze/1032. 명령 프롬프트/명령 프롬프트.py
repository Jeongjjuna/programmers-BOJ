import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
arr = []
for _ in range(n):
    arr.append(input().strip())


def main():
    base = list(arr[0])

    for i in range(len(base)):
        for j in range(1, n):
            if arr[j][i] == base[i]:
                continue

            base[i] = '?'
            break

    print(''.join(base))


if __name__ == "__main__":
    main()
