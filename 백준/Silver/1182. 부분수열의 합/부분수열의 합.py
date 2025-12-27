import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
visited = []
count = 0

def dfs(idx, sum):
    global count

    # 마지막 값을 넘어갔을 경우(즉, 이미 visited 가 n개가 전부 찼을 경우)
    if idx == n:
        # 크기가 양수인 부분수열 이므로, 전체가 False 이면 return
        # 이 부분은 매번 visited 를 전체 순회하지 않도록 최적화 가능함.(단 N <= 20 이므로 빠르게 구현)
        if not any(visited):
            return;

        if sum == s:
            count += 1
        return

    # idx 를 포함 하는 경우
    visited.append(True)
    dfs(idx + 1, sum + arr[idx])
    visited.pop()

    # idx 를 포함하지 않는 경우
    visited.append(False)
    dfs(idx + 1, sum)
    visited.pop()

def main():
    dfs(0, 0)
    print(count)

if __name__ == "__main__":
    main()