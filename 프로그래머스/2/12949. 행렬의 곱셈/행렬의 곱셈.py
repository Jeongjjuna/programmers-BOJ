def solution(arr1, arr2):
    
    m, k = len(arr1), len(arr1[0])
    k, n = len(arr2), len(arr2[0])
    
    answer = [[0]*n for _ in range(m)]
    
    
    '''
    [[2, 3, 2],
     [4, 2, 4], 
     [3, 1, 4]]
    '''
    
    '''
    [[5, 4, 3], 
     [2, 4, 1], 
     [3, 1, 1]]
    '''
    
    '''
    [[22, 22, 11], 
     [36, 28, 18], 
     [29, 20, 14]]
    
    '''
    
    
    for row in range(m):
        for col in range(n):
            
            val = 0
            for idx in range(k):
                # arr1[row][idx] # [2, 3, 2]
                # arr2[idx][col] # [5, 2, 3]
                val += arr1[row][idx] * arr2[idx][col]
            
            answer[row][col] = val
            
    
    return answer



