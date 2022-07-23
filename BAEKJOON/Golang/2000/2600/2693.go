package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var wr = bufio.NewWriter(os.Stdout)

func nextInt() int {
	sc.Scan()
	text := sc.Text()
	n, _ := strconv.Atoi(text)
	return n
}

func main() {
	sc.Split(bufio.ScanWords)
	defer wr.Flush()

	N := nextInt()
	for i := 0; i < N; i++ {
		var seq []int
		for j := 0; j < 10; j++ {
			seq = append(seq, nextInt())
		}
		sort.Ints(seq)
		fmt.Fprintln(wr, seq[7])
	}
}
