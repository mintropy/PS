package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)

	sc.Scan()
	t, _ := strconv.Atoi(sc.Text())
	for i := 0; i < t; i++ {
		sc.Scan()
		line := strings.Split(sc.Text(), " ")
		n, _ := strconv.ParseFloat(line[0], 32)
		for _, cmd := range line {
			if cmd == "@" {
				n *= 3
			} else if cmd == "%" {
				n += 5
			} else if cmd == "#" {
				n -= 7
			}
		}
		fmt.Printf("%.2f\n", n)
	}
}
