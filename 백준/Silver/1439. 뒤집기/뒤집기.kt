fun main() = with(System.`in`.bufferedReader()) {

    // 변수 입력 및 선언
    val str: List<Char> = readLine().toList()

    // 0001100 을 순회한다.
    val n = str.size
    val count = hashMapOf(
        '0' to 0,
        '1' to 0
    )
    for (i in 0 .. n - 2) {
        if (str[i] != str[i + 1]) {
            count[str[i]]  = count.getValue(str[i]) + 1
        }
    }
    count[str[n - 1]] = count.getValue(str[n - 1]) + 1

    println(count.values.min())
}