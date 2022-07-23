package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var wr = bufio.NewWriter(os.Stdout)

func main() {
	defer wr.Flush()

	sc.Split(bufio.ScanWords)
	sc.Scan()
	N := sc.Text()
	var numCheck [10]int
	var sum int
	for i := 0; i < len(N); i++ {
		r := N[i]
		n, _ := strconv.Atoi(string(r))
		sum += n
		numCheck[n]++
	}
	if numCheck[0] != 0 || sum%3 == 0 {
		for i := 9; i >= 0; i-- {
			for j := 1; j <= numCheck[i]; j++ {
				fmt.Fprint(wr, i)
			}
		}
	} else {
		fmt.Fprint(wr, -1)
	}
}
