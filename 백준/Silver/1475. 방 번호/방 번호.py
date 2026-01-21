import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = input().strip()


def main():
    arr = []
    for elem in n:
        if elem == '9':
            arr.append('6')
        else:
            arr.append(elem)

    count = {}
    for i in range(0, 9):
        count[str(i)] = 0

    for elem in arr:
        count[elem] += 1

    if count['6'] % 2 == 0:
        count['6'] = count['6'] // 2
    else:
        count['6'] = (count['6'] // 2) + 1

    answer = 0
    for i in count.values():
        answer = max(answer, i)

    print(answer)


if __name__ == "__main__":
    main()
