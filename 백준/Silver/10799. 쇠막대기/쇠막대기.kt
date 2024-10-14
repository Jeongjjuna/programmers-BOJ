fun main() = with(System.`in`.bufferedReader()) {

    // 변수 입력 및 선언
    val str: List<Char> = readLine().toList()
    var answer = 0

    // 스택을 순회한다.
    val stack = ArrayDeque<Char>() // addLast, removeLast

    for ((i, s) in str.withIndex()) {
        // ( 들어온 경우
        if (s == '(') {
            stack.addLast(s)
            continue
        }

        // 이전값이 (였는데 )가 들어오면 공
        if (str[i - 1] == '(') {
            stack.removeLast() // 공이라고 생각하고 제거
            answer += stack.size
        // 그렇지 않다면 막대가 끝남
        } else {
            // 막대가 끝나기 때문에 + 1
            stack.removeLast()
            answer += 1
        }
    }

    println(answer)

}