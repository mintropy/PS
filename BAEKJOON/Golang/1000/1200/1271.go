package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n, m big.Int
	fmt.Scanln(&n, &m)

	mul := new(big.Int)
	mod := new(big.Int)
	mul = mul.Div(&n, &m)
	mod = mod.Mod(&n, &m)

	fmt.Println(mul)
	fmt.Println(mod)
}
