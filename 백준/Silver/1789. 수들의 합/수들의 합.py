import sys; input = sys.stdin.readline

n = int(input())

# 그리디 풀이법(고민고민해볼것)
digit = 1
sum = 0
cnt = 0
while (sum <= n):
    sum += digit
    digit += 1
    cnt += 1

print(cnt - 1)