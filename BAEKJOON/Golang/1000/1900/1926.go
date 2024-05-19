package main

import (
	"bufio"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var wr = bufio.NewWriter(os.Stdout)

func nextInt() int {
	sc.Scan()
	text := sc.Text()
	r, _ := strconv.Atoi(text)
	return r
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func dfs(x, y int, board [][]int, visited [][]bool, delta [][]int) int {
	visited[x][y] = true
	size := 1

	for i := 0; i < 4; i++ {
		nx := x + delta[i][0]
		ny := y + delta[i][1]

		if board[nx][ny] == 1 && !visited[nx][ny] {
			size += dfs(nx, ny, board, visited, delta)
		}
	}

	return size
}

func main() {
	sc.Split(bufio.ScanWords)
	defer wr.Flush()

	N := nextInt()
	M := nextInt()

	board := make([][]int, N+2)
	board[0] = make([]int, M+2)
	board[N+1] = make([]int, M+2)

	for i := 0; i < N+2; i++ {
		board[i] = make([]int, M+2)

		for j := 0; j < M+2; j++ {
			board[i][j] = 0
		}
	}

	for i := 1; i < N+1; i++ {
		for j := 1; j < M+1; j++ {
			board[i][j] = nextInt()
		}
	}

	visited := make([][]bool, N+2)
	for i := 0; i < N+2; i++ {
		visited[i] = make([]bool, M+2)
	}

	delta := make([][]int, 4)
	delta[0] = []int{0, 1}
	delta[1] = []int{0, -1}
	delta[2] = []int{1, 0}
	delta[3] = []int{-1, 0}

	pieces := 0
	maxSize := 0

	for i := 1; i < N+1; i++ {
		for j := 1; j < M+1; j++ {
			if board[i][j] == 1 && !visited[i][j] {
				pieces++
				maxSize = max(maxSize, dfs(i, j, board, visited, delta))
			}
		}
	}

	wr.WriteString(strconv.Itoa(pieces) + "\n")
	wr.WriteString(strconv.Itoa(maxSize))
}
