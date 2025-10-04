package main

import "fmt"

func main() {
	var s string
	var n int
	fmt.Scanln(&s)
	fmt.Scanln(&n)
	if n < 1 || n > len(s) {
		fmt.Println("Error: n is out of range")
		return
	}
	fmt.Println(string(s[n-1]))
}
