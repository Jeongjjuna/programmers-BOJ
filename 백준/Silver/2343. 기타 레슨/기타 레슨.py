import sys; input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))


def check(mid):
    global m
    # mid만큼의 크기에 들어맞도록 arr를 m개로 나눈다.
    # m개로 제대로 나누어 지지 않으면 false

    used_m = 0
    interval_sum = 0
    for i in range(len(arr)):
        # 한 개의 숫자가 담으려는 블루레이보다 크다면 애초에 안되는것으로 간주한다.
        if arr[i] > mid:
            return False

        if interval_sum + arr[i] > mid:
            used_m += 1
            interval_sum = arr[i]
        else:
            interval_sum += arr[i]

        #print(f"{i}, intaval : {interval_sum}")

    if used_m + 1 <= m:
        return True
    else:
        return False
    

start, end = 1, 1000000000
ans = 0
while (start <= end):
    mid = (start + end) // 2
    
    if check(mid):
        end = mid -1
        ans = mid
    else:
        start = mid + 1


print(ans)