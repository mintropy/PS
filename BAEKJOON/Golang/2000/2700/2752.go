package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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

	var nums []int
	for i := 0; i < 3; i++ {
		nums = append(nums, nextInt())
	}
	sort.Ints(nums)
	for _, x := range nums {
		fmt.Fprint(wr, x, " ")
	}
}
