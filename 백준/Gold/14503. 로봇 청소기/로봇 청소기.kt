val dxs = intArrayOf(-1, 0, 1, 0)
val dys = intArrayOf(0, 1, 0, -1)
var count = 0

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map{ it.toInt() }
    var (x, y, d) = readLine().split(" ").map{ it.toInt() }
    val arr: Array<IntArray> = Array(n) { readLine().split(" ").map{ it.toInt() }.toIntArray() }


    while (true) {
        // 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if (arr[x][y] == 0) {
            arr[x][y] = 2
            count += 1
        }

        // 2. 주변 4칸 확인
        var isNotClean = false
        for ((dx, dy) in dxs.zip(dys)) {
            val nx = x + dx
            val ny = y + dy

            if (isRange(nx, ny, n, m) && arr[nx][ny] == 0) {
                isNotClean = true
                break
            }
        }

        // 3. 청소되지 않은 빈칸이 있는 경우
        if (isNotClean) {
            // 반시계 방향 회전
            d += 3
            d %= 4

            // 앞칸 청소되지 않은 빈 칸이면 전진
            val nx = x + dxs[d]
            val ny = y + dys[d]
            if (isRange(nx, ny, n, m) && arr[nx][ny] == 0) {
                x = nx
                y = ny
            }
            continue
        } else { // 빈칸이 없는 경우
            // 후진할 수 있따면, 한칸 후진
            val nx = x - dxs[d]
            val ny = y - dys[d]
            if (isRange(nx, ny, n, m) && arr[nx][ny] == 2) {
                x = nx
                y = ny
                continue
            }
            // 후진할 수 없다면
            break
        }
    }

    println(count)
}

fun isRange(x:Int, y: Int, n: Int , m: Int): Boolean {
    return x in 0 until n && y in 0 until  m
}