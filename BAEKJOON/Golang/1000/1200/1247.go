package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	zero := big.NewInt(0)
	for i := 0; i < 3; i++ {
		var tests int
		fmt.Fscan(reader, &tests)
		var sum, tmp big.Int
		for j := 0; j < tests; j++ {
			fmt.Fscan(reader, &tmp)
			sum = *sum.Add(&sum, &tmp)
		}
		if sum.Cmp(zero) == 0 {
			fmt.Fprintln(writer, 0)
		} else if sum.Cmp(zero) > 0 {
			fmt.Fprintln(writer, "+")
		} else {
			fmt.Fprintln(writer, "-")
		}
	}
}
