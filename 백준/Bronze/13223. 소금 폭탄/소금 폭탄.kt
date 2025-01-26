import java.io.*

private val scan = FastReader()
private val out = PrintWriter(System.out)

private var currTime = ""
private var targetTime = ""

fun timeToSeconds(time: String): Int {
    val parts: List<Int> = time.split(":").map { it.toInt() }
    val hours = parts[0]
    val minutes = parts[1]
    val seconds = parts[2]
    return hours * 3600 + minutes * 60 + seconds
}

fun secondsToTime(sec: Int): String {
    val hours = sec / 3600
    val minutes = (sec % 3600) / 60
    val seconds = sec % 60
    return String.format("%02d:%02d:%02d", hours, minutes, seconds)
}

fun main() {
    currTime = scan.nextLine()
    targetTime = scan.nextLine()
    // 초 단위로 변환
    val currTimeSec = timeToSeconds(currTime)
    val targetTimeSec = timeToSeconds(targetTime)

    if (currTimeSec < targetTimeSec) {
        out.println(secondsToTime(targetTimeSec - currTimeSec))
    } else {
        out.println(secondsToTime(targetTimeSec + 24 * 60 * 60 - currTimeSec))
    }

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