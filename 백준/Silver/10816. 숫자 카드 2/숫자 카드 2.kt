fun main() = with(System.`in`.bufferedReader()) {

    // 변수 입력 및 선언
    val n = readLine().toInt()
    val cards = readLine().split(" ").map { it.toInt() }
    val m = readLine().toInt()
    val targets = readLine().split(" ").map { it.toInt() }
    val count = mutableMapOf<Int, Int>()

    // 카운팅
    for (card in cards) {
        count[card] = count.getOrDefault(card, 0) + 1
    }

    // 개수 출력
    val answer = StringBuilder()
    var cnt = 0
    for (target in targets) {
        cnt = count.getOrDefault(target, 0)
        answer.append(cnt).append(" ")
    }

    println(answer)
}
