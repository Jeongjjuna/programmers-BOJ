import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
arr = []
dance = {}
for _ in range(n):
    a, b = input().split()
    arr.append((a, b))
    dance[a] = False
    dance[b] = False


def main():
    dance["ChongChong"] = True

    for (a, b) in arr:
        if dance[a] or dance[b]:
            dance[a] = True
            dance[b] = True

    # 춤을 추는 사람 찾기
    answer = 0
    for name in dance.keys():
        if dance[name]:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
