import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n, m = map(int, input().split())
matrix_a = []
for i in range(n):
    matrix_a.append(list(map(int, input().split())))
matrix_b = []
for i in range(n):
    matrix_b.append(list(map(int, input().split())))


def main():
    answer = [[None] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            answer[i][j] = matrix_a[i][j] + matrix_b[i][j]

    for elem in answer:
        print(*elem)


if __name__ == "__main__":
    main()
