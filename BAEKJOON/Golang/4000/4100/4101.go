package main

import "fmt"

func main() {
	for {
		var x, y int
		fmt.Scanf("%d %d", &x, &y)
		if x == 0 && y == 0 {
			break
		}
		if x > y {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
	}
}
