import sys; sys.setrecursionlimit(100000)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 분할정복으로 좌, 우 합치기
def find(arr, start, end):
    # arr의 start ~ end 범위에서 가장 큰 y의 idx찾기 O(n)
    if end < start:
        return None
    
    y_max_idx = -1
    y_max = -1
    for idx in range(start, end + 1):
        if y_max < arr[idx][2]:
            y_max = arr[idx][2]
            y_max_idx = idx
    
    root = Node(arr[y_max_idx][0])
    root.left = find(arr, start, y_max_idx - 1)
    root.right = find(arr, y_max_idx + 1, end)
    return root


def preorder(log, root):
    if root is None:
        return
    log.append(root.val)
    preorder(log, root.left)
    preorder(log, root.right)
    
    
def postorder(log, root):
    if root is None:
        return
    postorder(log, root.left)
    postorder(log, root.right)
    log.append(root.val)

    

def solution(nodeinfo): # 노드 개수 1만개
    # 1. 트리 만들기(인접리스트로 만들기)
    # arr = [(val, x, y)] 형태로 저장
    n = len(nodeinfo)
    arr = []
    for i in range(n):
        arr.append((i + 1, nodeinfo[i][0], nodeinfo[i][1]))
    
    # x 오름차순으로 정렬
    arr.sort(key = lambda x : x[1])

    # 루트노드 찾기
    root = find(arr, 0, n - 1)
    
    # 2. 전위순회하기 O(n)
    preorder_log = []
    preorder(preorder_log, root)
    
    # 3. 후위순회하기 O(n)
    postorder_log = []
    postorder(postorder_log, root)
    
    return [preorder_log, postorder_log]



# ---------------------- 테스트 -------------------
test_arr = [(6, 1, 3), (9, 2, 2), (4, 3, 5), (1, 5, 3), (5, 6, 1), (8, 7, 2), (7, 8, 6), (2, 11, 5), (3, 13, 3)]

find_node = find(test_arr, 0, 8)
# print(find_node.val)
# print(find_node.left.val)
# print(find_node.right.val)

# print(solution([[5, 5]]))