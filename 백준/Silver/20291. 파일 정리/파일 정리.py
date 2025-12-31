import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
arr = []
for _ in range(n):
    str = input().strip()
    # (파일이름, 확장자)
    arr.append(tuple(str.split(".")))


def main():
    count = dict()
    for _, extention in arr: # O(N)
        count[extention] = count.get(extention, 0) + 1

    sorted_count = sorted(count.items(), key=lambda x: x[0]) # O(NlogN)
    for extention, count in sorted_count: # O(N)
        print(extention, count)


if __name__ == "__main__":
    main()
