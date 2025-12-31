import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))


# O(N) + O(M)
def main():
    # 카드 개수 count O(N)
    count = dict()
    for elem in arr1:
        count[elem] = count.get(elem, 0) + 1

    answer = []
    for elem in arr2:  # O(M)
        count_in_cards = count.get(elem, 0)
        answer.append(count_in_cards)

    print(*answer)


if __name__ == "__main__":
    main()
