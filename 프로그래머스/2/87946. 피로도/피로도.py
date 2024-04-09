from itertools import permutations

# dungeons = ([80, 20], [50, 40], [30, 10])
def find_max_explore(k, dungeons):
    cnt = 0
    pre = k
    for elem in dungeons:
        if pre >= elem[0]:
            cnt += 1
            pre -= elem[1]
    return cnt


def solution(k, dungeons):
    answer = 0
    for elem in permutations(dungeons):
        answer = max(answer, find_max_explore(k, elem))
    return answer