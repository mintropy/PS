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

	M := nextInt()
	ans := 1
	for i := 0; i < M; i++ {
		a, b, t := nextInt(), nextInt(), nextInt()
		ans = ans * b / a
		if t == 1 {
			ans *= -1
		}
	}
	sign := 0
	if ans < 0 {
		sign = 1
		ans *= -1
	}
	fmt.Fprint(wr, sign, ans)
}
