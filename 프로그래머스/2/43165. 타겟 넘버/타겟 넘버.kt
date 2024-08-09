// 방법1. 완전탐색 + dfs
// 2**20 = 1048576

class Solution {
    
    private var answer = 0
    
    fun solution(numbers: IntArray, target: Int): Int {        
        dfs(numbers = numbers, target = target)
        return answer
    }
    
    fun dfs(numbers: IntArray, target: Int, sum: Int = 0, depth: Int = 0) {
        // 종료조건
        if (depth == numbers.size) {
            if (sum == target) {
                answer ++
            }
            return
        }
        
        // 재귀 탐색
        dfs(numbers, target, sum + numbers[depth], depth + 1)
        dfs(numbers, target, sum - numbers[depth], depth + 1)
    }
}