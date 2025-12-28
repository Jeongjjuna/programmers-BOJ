import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
visited = [False] * n
diag1 = [False] * (n * 2) # 우측 대각선 (row + col)
diag2 = [False] * (n * 2) # 좌측 대각선 (row - cal + n)
ansewr = 0


'''
(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)

(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)

(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)

(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)

(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)

(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)

(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)

(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)
'''


def dfs(row: int):
    global ansewr

    if (row == n):
        ansewr += 1
        return

    for col in range(n):
        # 같은 열에 존재한다면
        if visited[col]:
            continue

        # 우측 대각선에 존재한다면
        if diag1[row + col]:
            continue

        # 좌측 대각선에 존재한다면
        if diag2[row - col + n]:
            continue

        visited[col] = True
        diag1[row + col] = True
        diag2[row - col + n] = True
        dfs(row + 1)
        visited[col] = False
        diag1[row + col] = False
        diag2[row - col + n] = False

def main():
    global ansewr
    dfs(0)
    print(ansewr)

if __name__ == "__main__":
    main()
