import bisect
import sys

input = sys.stdin.readline
t = int(input())


# O(NlogM)
def main():
    for _ in range(t):
        n, m = map(int, input().split())  # n = 20000, m = 20000
        arr_a = list(map(int, input().split()))
        arr_b = list(map(int, input().split()))

        arr_b.sort()
        answer = 0
        for elem_a in arr_a:  # O(N)
            pos = bisect.bisect_left(arr_b, elem_a)  # O(logM)
            answer += pos

        print(answer)


if __name__ == "__main__":
    main()
