fun main() = with(System.`in`.bufferedReader()) {
    var sum = 0
    val arr = arrayListOf<Int>()
    repeat(9) {
        val n = readLine().toInt()
        sum += n
        arr.add(n)
    }

    // 거짓 난쟁이 2명 찾기
    val fix = mutableSetOf<Int>()
    for (i in 0 until 9) {
        for (j in i + 1 until  9) {
            if (sum - arr[i] - arr[j] == 100) {
                fix.add(arr[i])
                fix.add(arr[j])
            }
        }
    }

    // 거짓 난쟁이를 제외한 모든 난쟁이 출력
    for (elem in arr) {
        if (elem in fix) {
            continue
        }
        println(elem)
    }
}
