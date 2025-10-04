// Title : 문자와 문자열
// Link : https://www.acmicpc.net/problem/27866

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() =
        with(BufferedReader(InputStreamReader(System.`in`))) {
            val s = readLine()
            val i = readLine().toInt()

            println(s[i.toInt() - 1])
        }
