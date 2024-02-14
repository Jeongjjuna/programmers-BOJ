def find_fail_rate(i, count, prefix_sum):
    if prefix_sum[i] == 0:
        return 0
    return count[i] / prefix_sum[i]
    

def solution(N, stages):
    
    # 각 개수의 합 구하기
    # count = [1, 3, 2, 1, 0 ,1]
    count = [0] * (N + 2)
    for s in stages:
        count[s] += 1
    
    # 뒤에서 부터 누적합을 구한다.
    # prefix_sum = [8, 7, 4, 2, 1, 1]
    prefix_sum = [0] * (N + 2)
    prefix_sum[N + 1] = count[N + 1]
    for i in range(N, 0, -1):
        prefix_sum[i] = prefix_sum[i + 1] + count[i]
    
    # i번 스테이지와, i번 스테이지의 실패율을 쌍으로 구한다.
    fail_rates = []
    for i in range(1, N + 1):
        fail_rate = find_fail_rate(i, count, prefix_sum)
        fail_rates.append((fail_rate, i))
    
    
    # 정렬
    # 1. 실패율 내림차순
    # 2. 같으면 스테이지 작은 순으로 정렬
    fail_rates.sort(key = lambda x : (-x[0], x))

    
    return [elem[1] for elem in fail_rates]