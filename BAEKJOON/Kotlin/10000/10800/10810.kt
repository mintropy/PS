// Title : 공 넣기
// Link : https://www.acmicpc.net/problem/10810

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() =
        with(BufferedReader(InputStreamReader(System.`in`))) {
            val (n, m) = readLine().toString().split(" ").map { it.toInt() }
            val arr = IntArray(n)
            for (i in 0 until m) {
                val (a, b, c) = readLine().toString().split(" ").map { it.toInt() }
                for (j in a - 1 until b) {
                    arr[j] = c
                }
            }
            println(arr.joinToString(" "))
        }