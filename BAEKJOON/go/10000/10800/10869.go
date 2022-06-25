package main

import "fmt"

/*
Title : 사칙연산
Link : https://www.acmicpc.net/problem/10869
*/

func main() {
	var a, b int
	fmt.Scanln(&a, &b)
	fmt.Println(a + b)
	fmt.Println(a - b)
	fmt.Println(a * b)
	fmt.Println(a / b)
	fmt.Println(a % b)
}
