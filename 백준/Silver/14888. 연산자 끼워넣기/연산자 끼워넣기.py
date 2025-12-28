import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
min_result = sys.maxsize
max_result = -sys.maxsize

# 0 덧셈, 1 뺼샘, 2 곱셈, 3 나눗셈
arr = []
for i in range(4):
    count = operator[i]
    for _ in range(count):
        arr.append(i)

'''
중복이 혀용 배열의 순열 구하기
ex) 0 0 1 1 2 3 3
'''

def calculate(operators):
    # nums      [1, 2, 3, 4, 5, 6]
    # operators [3, 2, 0, 1, 0]
    num1 = nums[0]
    for i in range(0, len(nums) - 1):
        num2 = nums[i + 1]
        operator = operators[i]

        if (operator == 0):
            num1 = num1 + num2
        elif (operator == 1):
            num1 = num1 - num2
        elif (operator == 2):
            num1 = num1 * num2
        elif (operator == 3):
            if num1 < 0:
                num1 = -num1
                num1 = num1 //num2
                num1 = -num1
            else:
                num1 = num1 // num2
    return num1

def dfs(visited, curr):
    global min_result, max_result

    if len(curr) == n - 1:
        result = calculate(curr)
        min_result, max_result = min(min_result, result), max(max_result, result)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            curr.append(arr[i])
            dfs(visited, curr)
            visited[i] = False
            curr.pop()

def main():
    dfs([False] * (n - 1), [])
    print(max_result)
    print(min_result)

if __name__ == "__main__":
    main()
