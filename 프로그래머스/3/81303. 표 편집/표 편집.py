class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        
def connect(s, e):
    # s와 e를 이어줌
    if s is not None:
        s.right = e
    if e is not None:
        e.left = s

        
def move(c, size, selected):
    if c == "U":
        for _ in range(size):
            if selected.left is None:
                return selected
            selected = selected.left
        return selected
    
    elif c == "D":
        for _ in range(size):
            if selected.right is None:
                return selected
            selected = selected.right
        return selected
        
        
# 표의 행을 선택, 삭제, 복구
def solution(n, k, cmd):    
    
    nodes = [] # 초기 노드들을 담고있음
    selected = None # 현재선택된 Node주소
    deleted = [] # 삭제된 노드들을 stack형태로 관리
    
    # 1. 양방향 연결리스트 만들기
    for i in range(n):
        nodes.append(Node(i))
    for i in range(n - 1):
        connect(nodes[i], nodes[i + 1])
    selected = nodes[k]
    
    # 2. 시뮬레이션 돌리기
    for command in cmd:
        if command == "C":
            connect(selected.left, selected.right)
            deleted.append(selected)
            if selected.right is None:                    
                selected = selected.left
            else:
                selected = selected.right
            continue
            
        elif command == "Z":
            if len(deleted) == 0:
                continue
                
            restore_node = deleted.pop()
            left, right = restore_node.left, restore_node.right
            connect(left, restore_node)
            connect(restore_node, right)
            continue
        
        # 해당 거리만큼 이동(상, 하)
        c, size = command.split()
        selected = move(c, int(size), selected)
    
    
    check = ["X"] * n
    while selected.left is not None:
        selected = selected.left
    while selected.right is not None:
        check[selected.data] = "O"
        selected = selected.right
    check[selected.data] = "O"
    
    return "".join(check)