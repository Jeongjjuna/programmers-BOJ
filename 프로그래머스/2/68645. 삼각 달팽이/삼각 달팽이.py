def is_range(arr, n, nx, ny):
    return 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0
    
def solution(n):
    # 남, 동, 북서
    dx, dy = [1, 0, -1], [0, 1, -1]
    dire = 0
    arr = [[None] * n for _ in range(n)]
    for col in range(n):
        for row in range(col, n):
            arr[row][col] = 0
    
    # 시작값 세팅
    max_num = (n *(n + 1)) / 2
    num = 1
    dire = 0
    x, y = 0, 0
    arr[0][0] = num
    
    while num <= max_num:
        arr[x][y] = num
        
        nx, ny = x + dx[dire], y + dy[dire]
        if not is_range(arr, n, nx, ny):
            dire += 1
            dire %= 3
            nx, ny = x + dx[dire], y + dy[dire]
        
        x, y = nx, ny
        num += 1
    
    answer = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] is not None:
                answer.append(arr[i][j])

    return answer