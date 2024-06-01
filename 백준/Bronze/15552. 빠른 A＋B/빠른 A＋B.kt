import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.util.StringTokenizer

/**
 * kotlin 빠른 입출력
 */
val br = BufferedReader(InputStreamReader(System.`in`))
val bw = BufferedWriter(OutputStreamWriter(System.out))

fun main() {

    repeat(br.readLine().toInt()) {
        val st = StringTokenizer(br.readLine())
        val a = st.nextToken().toInt()
        val b = st.nextToken().toInt()
        val sum = a + b

        bw.write(sum.toString())
        bw.newLine()
    }

    bw.flush()

    br.close()
    bw.close()
}