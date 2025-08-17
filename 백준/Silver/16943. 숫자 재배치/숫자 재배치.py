from itertools import permutations
import sys

input = sys.stdin.readline

a, b = input().split()
b = int(b)

answer = -1

# a 문자열의 모든 순열 생성
for p in permutations(a, len(a)):
    if p[0] == '0':  # 0으로 시작하는 수 제외
        continue
    num = int(''.join(p))
    if num < b:
        answer = max(answer, num)

print(answer)