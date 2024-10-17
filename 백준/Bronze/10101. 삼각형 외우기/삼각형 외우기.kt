fun main() = with(System.`in`.bufferedReader()) {
    val a = readLine().toInt()
    val b = readLine().toInt()
    val c = readLine().toInt()

    if (a + b + c != 180) {
        println("Error")
        return
    } else if (a == b && b == c) {
        println("Equilateral")
    } else if (a == b || b == c || a == c) {
        println("Isosceles")
    } else {
        println("Scalene")
    }
}