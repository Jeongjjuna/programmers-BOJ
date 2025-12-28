import sys; input = sys.stdin.readline
sys.setrecursionlimit(1000000)


# pre_v : 현재 curr_nums에 포함된 모음개수
# pre_c : 현재 curr_nums에 포함된 자음개수
def dfs(start, curr_nums, pre_v, pre_c):
    global target_len

    # 1. 종료조건
    if len(curr_nums) == target_len:
        # 모음이 1개이상, 자음이 2개이상이라면
        if 1 <= pre_v and 2 <= pre_c:
            print("".join(curr_nums))
        return
    
    # 2. 재귀조건
    for i in range(start, len(arrs)):
        # 새로 추가될 값이 모음일 경우
        if arrs[i] in vowels:
            curr_nums.append(arrs[i])
            dfs(i + 1, curr_nums, pre_v + 1, pre_c)
            curr_nums.pop()
        # 새로 추가될 값이 자음일 경우
        else:
            curr_nums.append(arrs[i])
            dfs(i + 1, curr_nums, pre_v, pre_c + 1)
            curr_nums.pop()


target_len, C = map(int, input().split())
arrs = list(input().split())
vowels = "aeiou"

# ['a', 't', 'c', 'i', 's', 'w'] -> ['a', 'c', 'i', 's', 't', 'w']
arrs.sort()


dfs(0, [], 0, 0)