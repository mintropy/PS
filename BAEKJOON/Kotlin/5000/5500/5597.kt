// Title : 과제 안 내신 분..?
// Link : https://www.acmicpc.net/problem/5597

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() =
        with(BufferedReader(InputStreamReader(System.`in`))) {
                val students = BooleanArray(30)
                repeat(28) {
                        students[readLine().toInt() - 1] = true
                }
                students.forEachIndexed { index, b ->
                        if (!b) {
                        println(index + 1)
                        }
                }
        }