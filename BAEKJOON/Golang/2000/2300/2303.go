package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc *bufio.Scanner
	wr *bufio.Writer
)

func nextInt() int {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

func main() {
	sc = bufio.NewScanner(os.Stdin)
	wr = bufio.NewWriter(os.Stdout)

	sc.Split(bufio.ScanWords)
	defer wr.Flush()

	N := nextInt()
	var ans, maxUnitDigit int = 0, 0
	for i := 0; i < N; i++ {
		var card [5]int
		for j := 0; j < 5; j++ {
			card[j] = nextInt()
		}
		for x := 0; x < 5; x++ {
			for y := 0; y < 5; y++ {
				if x == y {
					continue
				}
				for z := 0; z < 5; z++ {
					if x == z || y == z {
						continue
					}
					unitDgit := (card[x] + card[y] + card[z]) % 10
					if maxUnitDigit <= unitDgit {
						ans = i + 1
						maxUnitDigit = unitDgit
					}
				}
			}
		}
	}
	fmt.Fprint(wr, ans)
}
