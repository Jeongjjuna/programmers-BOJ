import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.PrintWriter
import java.io.StreamTokenizer

private val scan = FastReader()
private val out = PrintWriter(System.out)

fun main() {
    val n = scan.nextInt()
    val m = scan.nextInt()
    val arr = IntArray(n) { it + 1 }
    repeat(m) {
        val num1 = scan.nextInt()
        val num2 = scan.nextInt()

        val temp = arr[num1 - 1]
        arr[num1 - 1] = arr[num2 - 1]
        arr[num2 - 1] = temp
    }

    out.println(arr.joinToString(" "))

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