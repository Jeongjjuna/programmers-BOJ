def make_stack_board(board, r, c):
    stack_board = []
    
    for i in range(c):
        stack = []
        for j in range(r - 1, -1, -1):
            if board[j][i] != 0:
                stack.append(board[j][i])
        stack_board.append(stack)
        
    return stack_board


def bomb(basket, selected):
    if len(basket) == 0:
        basket.append(selected)
        return 0
    
    if basket[-1] == selected:
        basket.pop()
        return 2
    else:
        basket.append(selected)
        return 0
    

'''
[[0,0,0,0,0],
[0,0,1,0,3],
[0,2,5,0,1],
[4,2,4,4,2],
[3,5,1,3,1]]

[1,5,3,5,1,2,1,4]
'''
def solution(board, moves):

    # 변수 입력 및 선언
    answer = 0
    r, c = len(board), len(board[0])
    
    
    # 전부 스택형태로 바꾸기
    '''
    [[3,4] 스택..
    [5,2,2] 스택..
    [1,4,5,1]
    [3,4]
    [1,2,1,3]]
    '''
    board = make_stack_board(board, r, c)
    
    
    basket = []
    for move in moves:
        move_idx = move - 1
        
        # 뽑을 게 없으면 패스
        if len(board[move_idx]) == 0:
            continue
        
        # 뽑아주기
        selected = board[move_idx].pop()
        
        # 뽑아준걸 바구니에 넣기(터진 개수를 반환)
        answer += bomb(basket, selected)
       
    
    return answer






