// Title : 최댓값
// link : https://www.acmicpc.net/problem/2566

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() =
    with(BufferedReader(InputStreamReader(System.`in`))) {
        var column = 0
        var row = 0
        var max = -1
        for (i in 1..9) {
            val arr = readLine().split(" ").map { it.toInt() }
            for (j in 1..9) {
                if (arr[j - 1] > max) {
                    max = arr[j - 1]
                    column = i
                    row = j
                }
            }
        }
        println(max)
        print("$column $row")
    }
