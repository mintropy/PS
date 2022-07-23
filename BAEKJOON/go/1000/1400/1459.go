package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var wr = bufio.NewWriter(os.Stdout)

func ArrayToNums(seq string) (int, int, int, int) {
	tmp := strings.Split(seq, " ")
	X, _ := strconv.Atoi(tmp[0])
	Y, _ := strconv.Atoi(tmp[1])
	W, _ := strconv.Atoi(tmp[2])
	S, _ := strconv.Atoi(tmp[3])
	return X, Y, W, S
}

func main() {
	defer wr.Flush()

	sc.Scan()
	text := sc.Text()
	X, Y, W, S := ArrayToNums(text)
	dist := 0
	if S < W*2 {
		var min, max int
		if X > Y {
			min, max = Y, X
		} else {
			min, max = X, Y
		}		dist += min * S
		if S < W {
			dist += int((max-min)/2) * 2 * S
			dist += ((max - min) % 2) * W
		} else {
			dist += (max - min) * W
		}
	} else {
		dist += (X + Y) * W
	}
	fmt.Fprint(wr, dist)
}
