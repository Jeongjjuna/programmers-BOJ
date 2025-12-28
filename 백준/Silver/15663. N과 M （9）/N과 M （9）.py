import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 변수 및 입력 선언
n, m = map(int, input().split())
arr = list(map(int, input().split()))
unique = set()


def dfs(curr: list, visited: list):
    if len(curr) == m:
        unique.add(tuple(curr))
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        curr.append(arr[i])
        dfs(curr, visited)
        visited[i] = False
        curr.pop()


def main():
    arr.sort()

    visited = [None] + [False] * n
    dfs([], visited)

    answer = [elem for elem in unique]
    answer.sort()
    for elem in answer:
        print(*elem)


if __name__ == "__main__":
    main()
