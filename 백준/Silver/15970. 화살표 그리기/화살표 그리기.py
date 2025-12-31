import sys

input = sys.stdin.readline

# 변수 및 입력 선언
n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))


# 시도1 : 완전탐색 -> O(N * N)
# 시도2 : 색깔별로 그룹화 시키자.(그럼 위치순으로 정렬해서 앞/뒤 에 있는것만 비교하면 될듯)
def main():
    # 색깔별, 위치 오름차순
    arr.sort(key=lambda x: (x[1], x[0]))  # O(NlogN)

    dist_sum = 0
    for idx, elem in enumerate(arr):  # O(N)
        position, color = elem[0], elem[1]

        # 맨앞(뒤에 같은 색깔 한개는 무조건 있음)
        if idx == 0:
            dist_sum += abs(position - arr[idx + 1][0])
        # 맨뒤(앞에 같은 색깔 한개는 무조건 있음)
        elif idx == n - 1:
            dist_sum += abs(position - arr[idx - 1][0])
        # 그외
        else:
            dist_min_color = sys.maxsize
            # 같은 색깔이라면
            if arr[idx - 1][1] == color:
                dist_min_color = min(dist_min_color, abs(position - arr[idx - 1][0]))
            # 같은 색깔이라면
            if arr[idx + 1][1] == color:
                dist_min_color = min(dist_min_color, abs(position - arr[idx + 1][0]))

            dist_sum += dist_min_color

    print(dist_sum)


if __name__ == "__main__":
    main()
