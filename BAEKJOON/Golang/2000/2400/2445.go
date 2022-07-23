package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	wr := bufio.NewWriter(os.Stdout)
	var N int

	defer wr.Flush()
	sc.Scan()
	fmt.Sscan(sc.Text(), &N)

	for i := 1; i <= N; i++ {
		for j := 0; j < i; j++ {
			wr.WriteByte('*')
		}
		for j := 0; j < N-i; j++ {
			wr.WriteByte(' ')
		}
		for j := 0; j < N-i; j++ {
			wr.WriteByte(' ')
		}
		for j := 0; j < i; j++ {
			wr.WriteByte('*')
		}
		wr.WriteByte('\n')
	}
	for i := N - 1; i > 0; i-- {
		for j := 0; j < i; j++ {
			wr.WriteByte('*')
		}
		for j := 0; j < N-i; j++ {
			wr.WriteByte(' ')
		}
		for j := 0; j < N-i; j++ {
			wr.WriteByte(' ')
		}
		for j := 0; j < i; j++ {
			wr.WriteByte('*')
		}
		wr.WriteByte('\n')
	}

}
