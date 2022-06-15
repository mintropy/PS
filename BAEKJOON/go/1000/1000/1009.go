package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	sc *bufio.Scanner
	wr *bufio.Writer
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)

	wr = bufio.NewWriter(os.Stdout)
}

func scanInt() int {
	sc.Scan()
	ret, _ := strconv.Atoi(sc.Text())
	return ret
}

func main() {
	defer wr.Flush()

	testCase := scanInt()
	for i := 0; i < testCase; i++ {
		a, b := scanInt(), scanInt()
		tmp := calcPower(a, b) % 10
		if tmp == 0 {
			wr.WriteString("10")
		} else {
			wr.WriteString(strconv.Itoa(tmp))
		}
		wr.WriteString("\n")
	}
}

func calcPower(a, b int) int {
	if a == 1 {
		return 1
	}
	if b == 1 {
		return a % 10
	}
	tmp := calcPower(a, b/2) % 10
	if b%2 == 0 {
		return (tmp * tmp) % 10
	}
	return (tmp * tmp * a) % 10
}
