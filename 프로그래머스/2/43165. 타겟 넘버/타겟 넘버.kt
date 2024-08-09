// 방법1. 완전탐색
// 2**20 = 1048576

class Solution {
    
    private var answer = 0
    
    fun solution(numbers: IntArray, target: Int): Int {        
        dfs(numbers, target, 0, 0)
        return this.answer
    }
    
    fun dfs(numbers: IntArray, target: Int, sum: Int, depth: Int) {
        if (depth == numbers.size) {
            if (sum == target) {
                this.answer += 1
            }
            return
        }
        
        dfs(numbers, target, sum + numbers[depth], depth + 1)
        dfs(numbers, target, sum - numbers[depth], depth + 1)
    }
}