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

func main() {
	sc.Split(bufio.ScanWords)
	defer wr.Flush()

	N, F := nextInt(), nextInt()
	_N := int(N/100) * 100
	if _N%F == 0 {
		fmt.Fprint(wr, "00")
	} else {
		ans := strconv.Itoa(_N + (F - _N%F))
		l := len(ans)
		fmt.Fprint(wr, ans[l-2:])
	}
}
