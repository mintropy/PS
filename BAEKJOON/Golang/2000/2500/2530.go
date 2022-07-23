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

	A, B, C, D := nextInt(), nextInt(), nextInt(), nextInt()
	now := A*60*60 + B*60 + C
	end := now + D
	H, M, S := (end/(60*60))%24, int((end%(60*60))/60), end%60
	fmt.Fprintln(wr, H, M, S)
}
