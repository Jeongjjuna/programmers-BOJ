from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = []
for i in arr:
    idx = bisect_left(dp, i)

    # 추가
    if idx == len(dp):
        dp.append(i)
    # 대체하기
    else:
        dp[idx] = i

print(len(dp))