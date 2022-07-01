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
	r, _ := strconv.Atoi(text)
	return r
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	sc.Split(bufio.ScanWords)
	defer wr.Flush()

	N := nextInt()
	answer := 0
	for i := 0; i < N; i++ {
		a, b, c := nextInt(), nextInt(), nextInt()
		tmp := 0
		if a == b && b == c && c == a {
			tmp = 10000 + 1000*a
		} else if a == b {
			tmp = 1000 + 100*a
		} else if b == c {
			tmp = 1000 + 100*b
		} else if c == a {
			tmp = 1000 + 100*c
		} else {
			tmp = 100 * max(a, max(b, c))
		}
		if answer < tmp {
			answer = tmp
		}
	}
	fmt.Fprint(wr, answer)
}
