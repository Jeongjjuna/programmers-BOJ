fun main() {
    val sum = readLine()!!.split(" ").sumOf { it.toInt() }
    println(sum)
}