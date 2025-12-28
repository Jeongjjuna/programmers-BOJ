import sys; input = sys.stdin.readline


def dfs(n, m, curr):
    if (len(curr) == m):
        print(*curr)
        return

    for i in range(curr[-1] + 1, n + 1):
        visited[i] = True
        curr.append(i)
        dfs(n, m, curr)
        curr.pop()
        visited[i] = False
    



n, m = map(int, input().split())
visited = [None] + [False] * n

for i in range(1, n + 1):
    dfs(n, m, [i])