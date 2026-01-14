import sys

input = sys.stdin.readline

# 변수 및 입력 선언
size = 9
arr = []
for i in range(size):
    arr.append(list(map(int, input().split())))


def main():
    nums = []
    for i in range(size):
        for j in range(size):
            nums.append((i + 1, j + 1, arr[i][j]))

    nums.sort(key=lambda x: -x[2])
    print(nums[0][2])
    print(nums[0][0], nums[0][1])


if __name__ == "__main__":
    main()
