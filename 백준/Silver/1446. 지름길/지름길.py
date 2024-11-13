from collections import deque
import heapq
import sys

input = sys.stdin.readline

# 변수 입력 및 선언
INT_MAX = sys.maxsize
n, target = map(int, input().split())

# 노드 정보
nodes = set()
nodes.add(0)
nodes.add(target)

# 지름길 정보 (시작, 끝, 가중치)
edges = set()

# 지름길 정보 입력받기
for _ in range(n):
    start, end, w = map(int, input().split())
    
    edges.add((start, end, w))

    nodes.add(start)
    nodes.add(end)

node_list = sorted(list(nodes))
num_of_nodes = len(nodes)
edges = list(edges)

# 인접 리스트 만들기
graph = dict()
dist = dict()
for elem in list(nodes):
    graph[elem] = []
    dist[elem] = INT_MAX

for (start, end, w) in edges:
    graph[start].append((end, w))

for i in range(len(node_list)-1):
    start = node_list[i]
    end = node_list[i + 1]
    graph[start].append((end, end - start))


# 다익스트라
pq = []
heapq.heappush(pq, (0, 0)) # (거리, 정점)
dist[0] = 0

while pq:
    min_dist, min_index = heapq.heappop(pq)

    if (min_dist != dist[min_index]):
        continue

    for next_index, next_dist in graph[min_index]:
        new_dist = dist[min_index] + next_dist
        if (new_dist < dist[next_index]):
            dist[next_index] = new_dist
            heapq.heappush(pq, (new_dist, next_index))

print(dist[target])