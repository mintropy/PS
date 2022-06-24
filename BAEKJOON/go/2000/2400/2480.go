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
	if x < y {
		return y
	}
	return x
}

func main() {
	sc.Split(bufio.ScanWords)
	defer wr.Flush()

	X, Y, Z := nextInt(), nextInt(), nextInt()
	if X == Y && Y == Z {
		fmt.Fprint(wr, 10000+1000*X)
	} else if X == Y {
		fmt.Fprint(wr, 1000+100*X)
	} else if Y == Z {
		fmt.Fprint(wr, 1000+100*Y)
	} else if Z == X {
		fmt.Fprint(wr, 1000+100*Z)
	} else {
		maxValue := max(X, max(Y, Z))
		fmt.Fprint(wr, 100*maxValue)
	}
}
