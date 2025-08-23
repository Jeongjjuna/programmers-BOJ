import sys
input = sys.stdin.readline

paper_count = int(input())
positions = []
for _ in range(paper_count):
    x, y = map(int, input().split())
    positions.append((x, y))

size = 1000
arr = [[0] * size for _ in range(size)]


# 기준점 500
for (x, y) in positions:
    nx, ny = x + 500, y + 100
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1


total = sum(cell for row in arr for cell in row)
print(total)