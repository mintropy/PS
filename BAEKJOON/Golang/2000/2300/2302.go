package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var (
	sc *bufio.Scanner
	wr *bufio.Writer
)

func nextInt() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

func solve(N int, M int, seats []int) int {
	var dp []int
	dp = append(dp, 1, 1)
	for i := 2; i < 41; i++ {
		dp = append(dp, dp[i-1]+dp[i-2])
	}
	sort.Slice(seats, func(i, j int) bool {
		return seats[i] < seats[j]
	})
	ans := 1
	for i := 0; i < M+1; i++ {
		x, y := seats[i], seats[i+1]
		ans *= dp[y-x-1]
	}
	return ans
}

func main() {
	sc = bufio.NewScanner(os.Stdin)
	wr = bufio.NewWriter(os.Stdout)

	sc.Split(bufio.ScanWords)
	defer wr.Flush()

	N := nextInt()
	M := nextInt()
	var seats []int
	for i := 0; i < M; i++ {
		k := nextInt()
		seats = append(seats, k)
	}
	seats = append(seats, 0, N+1)

	ans := solve(N, M, seats)
	fmt.Fprint(wr, ans)
}
