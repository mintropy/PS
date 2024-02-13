// Title : 바구니 뒤집기
// Link : https://www.acmicpc.net/problem/10811

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() =
    with(BufferedReader(InputStreamReader(System.`in`))) {
        val (n, m) = readLine().split(" ").map { it.toInt() }
        val arr = IntArray(n) { it + 1 }

        repeat(m) {
            val (i, j) = readLine().split(" ").map { it.toInt() }
            arr.slice(i - 1 until j).reversed().forEachIndexed { index, value ->
                arr[i - 1 + index] = value
            }
        }

        println(arr.joinToString(" "))
    }
