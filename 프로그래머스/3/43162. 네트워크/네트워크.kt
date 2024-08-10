class Solution {
    fun solution(n: Int, computers: Array<IntArray>): Int {
        var answer = 0
        
        // 연결 그래프를 생성한다.
        val arr = Array(n) { mutableListOf<Int>() }
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (i == j) continue
                
                if (computers[i][j] == 1) {
                    arr[i].add(j)
                    arr[j].add(i)
                }
            }
        }
        
        // 0 ~ n-1 의 방문 배열 생성
        val visited = BooleanArray(n)
        
        // 방문하지 않았다면, dfs 탐색
        for (i in 0 until n) {
            if (!visited[i]) {
                answer++
                visited[i] = true
                dfs(arr, visited, i)
            }
        }
        
        return answer
    }
    
    private fun dfs(
        arr: Array<MutableList<Int>>,
        visited: BooleanArray,
        v: Int
    ) {
        for (nv in arr[v]) {
            if (!visited[nv]) {
                visited[nv] = true
                dfs(arr, visited, nv)
            }
        }
    }
}