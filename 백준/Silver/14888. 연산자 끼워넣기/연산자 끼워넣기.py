import sys; input = sys.stdin.readline
from itertools import permutations

# 입력
n = int(input())
arr = list(map(int, input().split()))
num_four = list(map(int, input().split())) # +, -, x, % 의 개수

'''
수열의 순서를 바꾸면 안됨!!
연산자 우선순위를 무시하고 앞에서부터 계산한다!!
    나눗셈 할 때 몫(정수)만 취한다.
    음수를 양수로 나눌 때는 양수로 바꾸고 몫을 구하고, 그 몫을 음수로 바꾼다.

계산 결과의 최대와 최소를 구하라.

최대 O(10!) * O(n)

'''

# per_list = 연산자 순서경우의 수 구하기
com = []
for i, x in enumerate(num_four):
    for j in range(x):
        com.append(i)

per_list = []
for p in permutations(com, len(com)):
    per_list.append(p)

# per_list를 순회하며 각 연산의 최대, 최소값을 갱신해주기
ans_max, ans_min = -sys.maxsize, sys.maxsize
for x in per_list: #O(300만)
    # x = (0, 0, 1, 2, 3)
    # arr = 1 2 3 4 5 6
    ans = arr[0]
    for i in range(len(arr)-1):
        if x[i] == 0:
            ans = ans + arr[i+1]
            
        elif x[i] == 1:
            ans = ans - arr[i+1]

        elif x[i] == 2:
            ans = ans * arr[i+1]

        else:
            if ans < 0:
                ans = (-ans) // arr[i+1]
                ans = -(ans)
            else:
                ans = ans // arr[i+1]

    ans_max = max(ans_max, ans)
    ans_min = min(ans_min, ans)

print(ans_max)
print(ans_min)