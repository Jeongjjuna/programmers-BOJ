import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
min_val = sys.maxsize
max_val = -sys.maxsize

'''
중복이 혀용 배열의 순열 구하기
ex) 0 0 1 1 2 3 3
'''


def calculate(operand1: int, operand2: int, operator: int) -> int:
    if (operator == 0):
        return operand1 + operand2
    elif (operator == 1):
        return operand1 - operand2
    elif (operator == 2):
        return operand1 * operand2
    else:
        if operand1 < 0:
            return -((-operand1) // operand2)
        else:
            return operand1 // operand2


def dfs(dep: int, cal_result: int, visited: list):
    # 연산자를 전부 사용했다면
    if dep == n:
        global max_val, min_val
        max_val = max(max_val, cal_result)
        min_val = min(min_val, cal_result)
        return

    # 0 덧셈, 1 뺄셈, 2 곱셈, 3 나눗셈
    for i in range(4):
        operator_cnt = operator[i]
        if operator_cnt != 0:
            operator[i] -= 1
            visited.append(i)
            dfs(dep + 1, calculate(cal_result, nums[dep], i), visited)
            operator[i] += 1
            visited.pop()


def main():
    dfs(1, nums[0], [])
    print(max_val)
    print(min_val)


if __name__ == "__main__":
    main()
