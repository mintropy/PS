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
	v, _ := strconv.Atoi(text)
	return v
}

func main() {
	sc.Split(bufio.ScanWords)
	defer wr.Flush()

	A, B, C := nextInt(), nextInt(), nextInt()
	C += B
	A, B = A+C/60, C%60
	A %= 24
	fmt.Fprint(wr, A, B)
}
