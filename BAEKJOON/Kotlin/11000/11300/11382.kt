import java.io.BufferedReader
import java.io.InputStreamReader

fun main() =
        with(BufferedReader(InputStreamReader(System.`in`))) {
            val (a, b, c) = readLine().toString().split(" ").map { it.toLong() }
            println(a + b + c)
        }
