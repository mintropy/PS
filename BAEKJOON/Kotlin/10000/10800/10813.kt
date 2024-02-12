// Title : 공 바꾸기
// Link : https://www.acmicpc.net/problem/10813

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() =
        with(BufferedReader(InputStreamReader(System.`in`))) {
                val (n, m) = readLine().split(" ").map { it.toInt() }
                val balls = IntArray(n) { it + 1 }
        
                repeat(m) {
                        val (i, j) = readLine().split(" ").map { it.toInt() }
                        balls[i - 1] = balls[j - 1].also { balls[j - 1] = balls[i - 1] }
                }
        
                println(balls.joinToString(" "))
        }