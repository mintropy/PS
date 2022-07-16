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

	sc.Scan()
	text := sc.Text()
	t, _ := strconv.Atoi(text)

	if t%10 != 0 {
		fmt.Fprint(wr, -1)
	} else {
		a, b, c := t/300, (t%300)/60, (t%60)/10
		fmt.Fprint(wr, a, b, c)
	}
}
