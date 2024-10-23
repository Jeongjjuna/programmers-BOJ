import sys; input = sys.stdin.readline


def dfs(n, m, visited, curr):
    if (len(curr) == m):
        print(*curr)
        return

    for i in range(1, n + 1):
        if (visited[i]):
            continue
        visited[i] = True
        curr.append(i)
        dfs(n, m, visited, curr)
        curr.pop()
        visited[i] = False



n, m = map(int, input().split())
visited = [None] + [False] * n
dfs(n, m, visited, [])