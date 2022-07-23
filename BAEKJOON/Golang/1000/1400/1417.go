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
	dasom := nextInt()
	var votes [101]int
	for i := 0; i < N-1; i++ {
		v := nextInt()
		votes[v]++
	}
	answer := 0
	for i := 100; i > 0; i-- {
		if votes[i] == 0 {
			continue
		}
		for votes[i] > 0 {
			if dasom > i {
				break
			}
			dasom++
			votes[i]--
			votes[i-1]++
			answer++
		}
		if (votes[i] > 0 && dasom >= i) || dasom > i {
			break
		}
	}
	fmt.Fprint(wr, answer)
}
