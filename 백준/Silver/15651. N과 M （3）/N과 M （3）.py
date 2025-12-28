import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 변수 및 입력 선언
n, m = map(int, input().split())

def dfs(curr: list, visited: list):
    if len(curr) == m:
        print(*curr)
        return

    # 중복 없어야함. 오름차순 이어야함.
    for i in range(1, n + 1):
        visited[i] = True
        curr.append(i)
        dfs(curr, visited)
        visited[i] = False
        curr.pop()

def main():
    visited = [None] + [False] * n
    dfs([], visited)

if __name__ == "__main__":
    main()