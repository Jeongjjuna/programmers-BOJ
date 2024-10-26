import kotlin.math.abs

var count = 0

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()

    // (Col -> Row)
    val visited = IntArray(n) { -1 }

    nQueen(0, visited, n)

    println(count)
}

fun nQueen(row: Int, visited: IntArray, n: Int) {

    if (row == n) {
        count += 1
        return
    }

    for (col in 0 until n) {
        if (canGo(visited, row, col)) {
            visited[col] = row
            nQueen(row + 1, visited, n)
            visited[col] = -1
        }
    }
}

fun canGo(visited: IntArray, row: Int, col: Int): Boolean {
    // 이미 방문한 열인지 체크
    if (visited[col] != -1) {
        return false
    }

    // 대각선 관계에 있는지 체크
    for ((prevCol, prevRow) in visited.withIndex()) {
        if (prevRow == -1) {
            continue
        }

        if (abs(prevRow - row) == abs(prevCol - col)) {
            return false
        }
    }

    return true
}