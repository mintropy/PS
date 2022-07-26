package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var wr = bufio.NewWriter(os.Stdout)

func nextInts() [3]int {
	sc.Scan()
	text := sc.Text()
	tmp := strings.Split(text, " ")
	var nums [3]int
	for i, x := range tmp {
		n, _ := strconv.Atoi(x)
		nums[i] = n
	}
	return nums
}

func IntPow(x int) float64 {
	return float64(x * x)
}

func main() {
	sc.Split(bufio.ScanLines)
	defer wr.Flush()

	end := [3]int{0, 0, 0}
	triangleNum := 1
	for {
		nums := nextInts()
		if nums == end {
			break
		}
		fmt.Fprintf(wr, "Triangle #%d\n", triangleNum)
		triangleNum++
		if nums[2] == -1 {
			fmt.Fprintf(wr, "c = %.3f\n", math.Sqrt(IntPow(nums[0])+IntPow(nums[1])))
		} else if nums[0] == -1 {
			if nums[1] >= nums[2] {
				fmt.Fprint(wr, "Impossible.\n")
			} else {
				fmt.Fprintf(wr, "a = %.3f\n", math.Sqrt(IntPow(nums[2])-IntPow(nums[1])))
			}
		} else if nums[1] == -1 {
			if nums[0] >= nums[2] {
				fmt.Fprint(wr, "Impossible.\n")
			} else {
				fmt.Fprintf(wr, "b = %.3f\n", math.Sqrt(IntPow(nums[2])-IntPow(nums[0])))
			}
		}
		fmt.Fprint(wr, "\n")
	}
}
