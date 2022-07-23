package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scaner := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var N, M int
	fmt.Scanln(&N, &M)

	seq := make([][]int, N)
	for i := range seq {
		seq[i] = make([]int, M)
	}
	var tmp int
	for k := 0; k < 2; k++ {
		for i := 0; i < N; i++ {
			for j := 0; j < M; j++ {
				fmt.Fscan(scaner, &tmp)
				seq[i][j] += tmp
			}
		}
	}
	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			fmt.Fprint(writer, seq[i][j], " ")
		}
		fmt.Fprintln(writer)
	}
}
