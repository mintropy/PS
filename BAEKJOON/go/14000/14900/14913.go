package main

import (
	"bufio"
	"fmt"
	"os"
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

	a, d, k := nextInt(), nextInt(), nextInt()
	diff := k - a
	q, r := diff/d, diff%d
	if r != 0 || q < 0 {
		fmt.Fprint(wr, "X")
	} else {
		fmt.Fprint(wr, q+1)
	}
}
