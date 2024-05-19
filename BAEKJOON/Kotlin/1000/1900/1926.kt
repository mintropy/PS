// Title : 그림
// Link : https://www.acmicpc.net/problem/1926

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() =
    with(BufferedReader(InputStreamReader(System.`in`))) {
        val (n, m) = readLine().split(" ").map { it.toInt() }
        val board = Array(n) { readLine().split(" ").map { it.toInt() }.toIntArray() }

        val visited = Array(n) { BooleanArray(m) { false } }
        val dx = intArrayOf(0, 0, 1, -1)
        val dy = intArrayOf(1, -1, 0, 0)

        fun dfs(
            x: Int,
            y: Int,
        ): Int {
            visited[x][y] = true
            var size = 1

            for (i in 0 until 4) {
                val nx = x + dx[i]
                val ny = y + dy[i]

                if (nx in 0 until n && ny in 0 until m && !visited[nx][ny] && board[nx][ny] == 1) {
                    size += dfs(nx, ny)
                }
            }

            return size
        }

        var count = 0
        var maxSize = 0
        for (i in 0 until n) {
            for (j in 0 until m) {
                if (!visited[i][j] && board[i][j] == 1) {
                    count++
                    maxSize = maxOf(maxSize, dfs(i, j))
                }
            }
        }

        println("$count\n$maxSize")
    }
