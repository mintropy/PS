package main

import (
	"bufio"
	"os"
)

var sc = bufio.NewScanner(os.Stdin)
var wr = bufio.NewWriter(os.Stdout)

func main() {
	sc.Split(bufio.ScanLines)
	defer wr.Flush()

	var seq []string
	for i := 0; i < 5; i++ {
		sc.Scan()
		tmp := sc.Text()
		seq = append(seq, tmp)
	}
	for j := 0; j < 15; j++ {
		for i := 0; i < 5; i++ {
			if j < len(seq[i]) {
				wr.WriteByte(seq[i][j])
			}
		}
	}
}
