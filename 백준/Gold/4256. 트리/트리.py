import sys; input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def find_postorder(prior, preorder, start, end):
    global ans

    if start > end:
        return
    elif start == end:
        ans.append(preorder[start])
        return
    
    v = preorder[start]

    right = None
    for i in range(start + 1, end + 1):
        elem = preorder[i]
        if prior[v] < prior[elem]:
            right = i
            break
    
    if right is None:
        find_postorder(prior, preorder, start + 1, end)
    else:
        find_postorder(prior, preorder, start + 1, right - 1)
        find_postorder(prior, preorder, right, end)
    ans.append(v)


# 변수 입력 및 선언
t = int(input())
for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    # 중위순회로부터 해당 숫자 인덱스를 반환   
    prior = dict()
    for idx, elem in enumerate(inorder):
        prior[elem] = idx

    ans = []
    find_postorder(prior, preorder, 0, n - 1)
    print(*ans)