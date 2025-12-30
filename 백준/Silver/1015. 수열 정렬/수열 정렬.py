import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))


def main():
    answer = []
    sorted_arr = sorted(arr)  # 1 1 2 3
    pos = dict()
    for idx, elem in enumerate(sorted_arr):
        if elem not in pos:
            pos[elem] = deque()
        pos[elem].append(idx)
    # pos = {값 : [위치], 값 : [위치1, 위치2]}

    # 두번째 찾을때는 두번째 인덱스에서 찾아야함.
    for elem in arr:
        # elem 의 위치를 sorted_arr 에서 찾기
        index = pos[elem].popleft()
        answer.append(index)

    print(*answer)


if __name__ == "__main__":
    main()
