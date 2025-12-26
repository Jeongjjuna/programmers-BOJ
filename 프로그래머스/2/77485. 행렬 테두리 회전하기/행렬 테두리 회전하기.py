
def rotate(matrix, query):
    start_row, start_col, end_row, end_col = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1

    # 이동한 값들을 저장할 리스트
    moved_values = []

    # 직사각형 가장 왼쪽 위 모서리 값
    temp = matrix[start_row][start_col]
    moved_values.append(temp)
    
    # 직사각형 가장 왼쪽 열을 위로 한 칸씩 shift
    for row in range(start_row, end_row):
        matrix[row][start_col] = matrix[row + 1][start_col]
        moved_values.append(matrix[row][start_col])
    
    # 직사각형 가장 아래 행을 왼쪽으로 한 칸씩 shift
    for col in range(start_col, end_col):
        matrix[end_row][col] = matrix[end_row][col + 1]
        moved_values.append(matrix[end_row][col])
    
    # 직사각형 가장 오른쪽 열을 아래로 한 칸씩 shift
    for row in range(end_row, start_row, -1):
        matrix[row][end_col] = matrix[row - 1][end_col]
        moved_values.append(matrix[row][end_col])
    
    # 직사각형 가장 위 행을 오른쪽으로 한 칸씩 shift
    for col in range(end_col, start_col, -1):
        matrix[start_row][col] = matrix[start_row][col - 1]
        moved_values.append(matrix[start_row][col])
    
    # temp를 가장 왼쪽 위 모서리를 기준으로 바로 오른쪽 칸에 삽입
    matrix[start_row][start_col + 1] = temp
    moved_values.append(temp)

    # 이동한 값 중 최솟값 반환
    return min(moved_values)


def solution(rows, columns, queries):
    # 1. 행렬 만들기
    num = 1
    matrix = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = num
            num += 1

    # 2. 순차적으로 회전시키기
    answer = []
    for query in queries:
        min_value = rotate(matrix, query)
        answer.append(min_value)

    return answer


# case1
assert solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]) == [8, 10, 25]

# case2
assert solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]) == [1, 1, 5, 3]

# case3
assert solution(100,97,[[1,1,100,97]]) == [1]