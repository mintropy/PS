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

	N := nextInt()
	ans := 0
	for i := 0; i < 5; i++ {
		k := nextInt()
		if k == N {
			ans++
		}
	}
	fmt.Fprint(wr, ans)
}
