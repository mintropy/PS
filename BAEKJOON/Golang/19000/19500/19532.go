package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	var a, b, c, d, e, f int
	fmt.Fscan(r, &a, &b, &c, &d, &e, &f)
	x := (c*e - b*f) / (a*e - b*d)
	y := (a*f - c*d) / (a*e - b*d)
	fmt.Fprintf(w, "%d %d\n", x, y)
}
