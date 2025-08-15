import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.PrintWriter
import java.io.StreamTokenizer

private val scan = FastReader()
private val out = PrintWriter(System.out)

fun reverse(arr: IntArray, start: Int, end: Int): IntArray {
    var i = start - 1
    var j = end - 1
    while (i < j) {
        val tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i++
        j--
    }
    return arr
}

fun main() {
    val n = scan.nextInt()
    val m = scan.nextInt()
    val arr = IntArray(n) { it + 1 }

    repeat(m) {
        val a = scan.nextInt()
        val b = scan.nextInt()

        reverse(arr, a, b)
    }

    print(arr.joinToString(" "))

    scan.close()
    out.close()
}

class FastReader() {
    private val reader = BufferedReader(InputStreamReader(System.`in`))
    private val tokenizer = StreamTokenizer(reader)

    fun nextString(): String {
        tokenizer.nextToken()
        return tokenizer.sval
    }

    fun nextInt(): Int {
        tokenizer.nextToken()
        return tokenizer.nval.toInt()
    }

    fun nextLine(): String {
        return reader.readLine()
    }

    fun close() {
        reader.close()
    }
}