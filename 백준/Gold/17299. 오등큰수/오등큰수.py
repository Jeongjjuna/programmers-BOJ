'''
code.plus 알고리즘 기초 - 자료구조
백준(17299) - 오등큰수

[풀이] - 스택활용
A = [1, 1, 2, 3, 4, 2, 1]
F = [3, 3, 2, 1, 1, 2, 3]

<스택 순서>
- 실제 저장할 때에는 F배열의 (인덱스, 값) 으로 스택에 저장한다.
- 스택에 값을 삽입할 때 비교해서 오등큰수를 갱신한다.
[3]
[3, 3]
[3, 3, 2]
[3, 3, 2, 1]
[3, 3, 2, 1, 1]
[3, 3, 2, 1] <- 2 
[3, 3, 2]
[3, 3, 2, 2]
[3, 3, 2] <- 3
[3, 3]
[3, 3, 3] => [(0, 3), (1, 3) (6, 3)]

즉, 0, 1, 6 위치는 -1이 확실하다.
[-1, -1, ?, ?, ?, ?, -1]

? 부분은 초기값으로 -1을 채워준다.
'''

from collections import defaultdict


def create_frequency_arr(arr):
    d = defaultdict(int)
    for elem in arr:
        d[elem] += 1
    
    frequency_arr = []
    for elem in arr:
        frequency_arr.append(d[elem])
    
    return frequency_arr


def is_empty(stack):
    return len(stack) == 0


def main():
    n = int(input())
    A = list(map(int, input().split()))
    F = create_frequency_arr(A)
    NA = -1

    answer = [NA] * n
    
    stack = []
    for idx, elem in enumerate(F):
        if is_empty(stack):
            stack.append((idx, elem))
            continue

        while not is_empty(stack) and stack[-1][1] < elem:
            pop_data = stack.pop()
            answer[pop_data[0]] = A[idx]

        stack.append((idx, elem))

    print(*answer)

# 실행
main()

# 테스트
assert create_frequency_arr([1, 1, 2, 3, 4, 2, 1]) == [3, 3, 2, 1, 1, 2, 3]