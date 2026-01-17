import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
arr = []  # 출입기록 Baha enter
for _ in range(n):
    arr.append(tuple(input().split()))


def main():
    company = {}
    for (name, cmd) in arr:
        if cmd == "enter":
            company[name] = True
        else:  # leave
            company[name] = False

    result = []
    for name, exist in company.items():
        if exist:
            result.append(name)

    # 사전순의 역순
    result.sort(reverse=True)
    for name in result:
        print(name)


if __name__ == "__main__":
    main()
