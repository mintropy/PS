// Title : 코딩은 체육과목 입니다
// Link : https://www.acmicpc.net/problem/25314

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder

fun main() =
        with(BufferedReader(InputStreamReader(System.`in`))) {
            val N = readLine().toInt()
            val output = StringBuilder()
            repeat(N / 4) {
                output.append("long ")
            }
            output.append("int")
            println(output.toString())
        }
