import java.io.*

private val scan = FastReader()
private val out = PrintWriter(System.out)

private var words = ""
private var keyword = ""

fun main() {
    words = scan.nextLine()
    keyword = scan.nextLine()

    var count = 0
    var i = 0
    while(i + keyword.length <= words.length) {
        if (keyword == words.substring(i, i + keyword.length)) {
            count += 1
            i += keyword.length
        } else {
            i += 1
        }
    }

    out.println(count)

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