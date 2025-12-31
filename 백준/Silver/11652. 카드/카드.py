import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


def main():
    # 요소의 개수 dict (요소, 개수)
    count = dict()
    for elme in arr:
        count[elme] = count.get(elme, 0) + 1

    # 최빈값 찾기
    # 1순위 빈도수
    # 2순위 작은값순
    answer = max(count.items(), key=lambda x: (x[1], -x[0]))
    print(answer[0])


if __name__ == "__main__":
    main()
