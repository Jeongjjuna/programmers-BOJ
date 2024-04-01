import heapq
import sys

INT_MAX = sys.maxsize



# 다익스트라 수행 후 K시간 이내 거리 개수 구하면 될 듯?
def solution(N, road, K):
    
    # 인접 리스트 만들기
    arr = [[] for _ in range(N + 1)]
    for elem in road:
        a, b, w = elem[0], elem[1], elem[2]
        arr[a].append((b, w))
        arr[b].append((a, w))
    
    # 최단경로 측정
    start = 1
    pq = []
    heapq.heappush(pq, (0, start))
    distance = [INT_MAX] * (N + 1)
    distance[start] = 0
    
    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] != dist:
            continue
            
        for nv, w in arr[now]:
            if dist + w < distance[nv]:
                distance[nv] = dist + w
                heapq.heappush(pq, (dist + w, nv))
    
    answer = 0
    for i in range(2, N + 1):
        if distance[i] <= K:
            answer += 1
    
    return answer + 1