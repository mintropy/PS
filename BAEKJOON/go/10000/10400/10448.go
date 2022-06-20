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
	v, _ := strconv.Atoi(text)
	return v
}

func findTriangulars(triangularNumbers []int, K int) int {
	for _, x := range triangularNumbers {
		for _, y := range triangularNumbers {
			for _, z := range triangularNumbers {
				if x+y+z == K {
					return 1
				}
			}
		}
	}
	return 0
}

func main() {
	sc.Split(bufio.ScanWords)
	defer wr.Flush()

	var triangularNumbers []int
	triangularNumbers = append(triangularNumbers, 1)
	for i := 2; triangularNumbers[i-2] < 1000; i++ {
		triangularNumbers = append(triangularNumbers, triangularNumbers[i-2]+i)
	}
	testCase := nextInt()
	for i := 0; i < testCase; i++ {
		K := nextInt()
		fmt.Fprintln(wr, findTriangulars(triangularNumbers, K))
	}
}
