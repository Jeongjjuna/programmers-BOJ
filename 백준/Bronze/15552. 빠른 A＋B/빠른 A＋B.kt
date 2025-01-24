import java.io.*

private var N = 0
private var a = 0
private var b = 0

fun main() {
    val sb = StringBuilder()

    BufferedReader(InputStreamReader(System.`in`)).use {
        val scan = FastReader(it)

        N = scan.nextInt()
        repeat(N) {
            a = scan.nextInt()
            b = scan.nextInt()
            sb.append(a + b).appendLine()
        }
    }

    println(sb)
}

fun input() {
    BufferedReader(InputStreamReader(System.`in`)).use {
        val scan = FastReader(it)
    }
}

class FastReader(private val reader: BufferedReader) {
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
}