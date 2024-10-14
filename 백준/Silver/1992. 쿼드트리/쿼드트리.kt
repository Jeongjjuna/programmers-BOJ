fun main() = with(System.`in`.bufferedReader()) {

    // 변수 입력 및 선언
    val n = readLine().toInt()
    val arr: MutableList<IntArray>  = mutableListOf<IntArray>()
    repeat(n) {
        arr.add(readLine().toList().map { it.digitToInt() }.toIntArray())
    }

    // 풀이 : 분할정복
    val answer = findQuadTree(arr, 0, 0, n - 1, n - 1)
    println(answer)

//    val input = mutableListOf(
//        intArrayOf(1, 1, 1, 1, 0, 0, 0, 0),
//        intArrayOf(1, 1, 1, 1, 0, 0, 0, 0),
//        intArrayOf(0, 0, 0, 1, 1, 1, 0, 0),
//        intArrayOf(0, 0, 0, 1, 1, 1, 0, 0),
//        intArrayOf(1, 1, 1, 1, 0, 0, 0, 0),
//        intArrayOf(1, 1, 1, 1, 0, 0, 0, 0),
//        intArrayOf(1, 1, 1, 1, 0, 0, 1, 1),
//        intArrayOf(1, 1, 1, 1, 0, 0, 1, 1),
//    )
//    require(findQuadTree(input, 0, 4, 3, 7) == "(0010)")
//    require(findQuadTree(input, 0, 0, 3, 3) == "(110(0101))")
//    require(findQuadTree(input, 0, 0, 3, 3) == "(110(0101))")
//    require(findQuadTree(input, 0, 0, 1, 1) == "1")
//    require(findQuadTree(input, 0, 0, 0, 0) == "1")
//    require(findQuadTree(input, 0, 7, 0, 7) == "0")
//
//    require(allSame(input, 0, 0, 1, 1) == true)
//    require(allSame(input, 2, 2, 3, 3) == false)
//    require(allSame(input, 0, 0, 0, 0) == true)
//    require(allSame(input, 1, 1, 1, 1) == true)
}


fun findQuadTree(
    arr: MutableList<IntArray>,
    startX: Int,
    startY: Int,
    endX: Int,
    endY: Int
): String {
    // 전부 같은 값이라면
    if (allSame(arr, startX, startY, endX, endY)) {
        return arr[startX][startY].toString()
    }

    val midX = (startX + endX) / 2
    val midY = (startY + endY) / 2

    val leftUp = findQuadTree(arr, startX, startY, midX, midY)
    val rightUP = findQuadTree(arr, startX, midY + 1, midX, endY)
    val leftBottom = findQuadTree(arr, midX + 1, startY, endX, midY)
    val rightBottom = findQuadTree(arr, midX + 1, midY + 1, endX, endY)

    return "($leftUp$rightUP$leftBottom$rightBottom)"
}

fun allSame(
    arr: MutableList<IntArray>,
    startX: Int,
    startY: Int,
    endX: Int,
    endY: Int
): Boolean {
    val temp = arr[startX][startY]
    for (i in startX .. endX) {
        for (j in startY .. endY) {
            if (temp != arr[i][j]) {
                return false
            }
        }
    }
    return true
}