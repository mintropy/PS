package main

import (
	"fmt"
	"strings"
)

func main() {
	var A, B, cmd string

	fmt.Scanln(&A)
	fmt.Scanln(&cmd)
	fmt.Scanln(&B)

	aLength := len(A)
	bLength := len(B)
	if cmd == "*" {
		fmt.Print("1" + strings.Repeat("0", aLength+bLength-2))
	} else if A == B {
		fmt.Print("2" + strings.Repeat("0", aLength-1))
	} else if cmd == "+" {
		if aLength > bLength {
			aLength, bLength = bLength, aLength
		}
		fmt.Print("1" + strings.Repeat("0", bLength-aLength-1) + "1" + strings.Repeat("0", aLength-1))
	}
}
