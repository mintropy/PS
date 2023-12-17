// Title : 영수증
// Link : https://www.acmicpc.net/problem/25304

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() =
        with(BufferedReader(InputStreamReader(System.`in`))) {
            val X = readLine().toString().toInt()
            val N = readLine().toString().toInt()

            var total_price = 0
            for (i in 1..N) {
                val (price, count) = readLine().toString().split(" ").map { it.toInt() }
                total_price += price * count
            }
            val answer = if (total_price == X) "Yes" else "No"
            println(answer)
        }
