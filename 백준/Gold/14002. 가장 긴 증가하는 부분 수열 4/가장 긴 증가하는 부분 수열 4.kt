import kotlin.math.max

/**
 * 백준(14002) - 가장 긴 증가하는 부분 수열4
 *
 * [풀이] - DP
 * 1. DP 배열에 최대 증가 길이를 구한다.
 * 2. DP 배열을 역순으로 참조하여 최대 증가 길이에 해당하는
 *    가장 긴 증가 수열을 구한다.
 */
fun main() {
    // 변수 입력 및 선언
    val n = readln().toInt()
    val arr = readln().split(" ").map { it.toInt() }
    val dp = Array(n) { 1 }

    // 가장 긴 증가하는 수열의 최대 길이 dp구하기
    for (i in 1..<n) {
        for (j in 0..<i) {
            if (arr[j] < arr[i]) {
                dp[i] = max(dp[i], dp[j] + 1)
            }
        }
    }

    // dp = [1, 2, 1, 3, 2, 4]
    val longestLen = dp.max()
    var longest = longestLen
    val longests = mutableListOf<Int>()

    // 가장 긴 부분 수열 구하기
    for (i in n - 1 downTo 0) {
        if (dp[i] == longest) {
            longests.add(0, arr[i])
            longest -= 1
        }
    }

    // 출력
    println(longestLen)
    println(longests.joinToString(" ") )
}