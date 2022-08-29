package main

import "fmt"

func main() {
	var t int
	fmt.Scanf("%d", &t)

	for i := 0; i < t; i++ {
		var n int
		fmt.Scanf("%d", &n)
		var name string
		var maxAlcohol int
		maxAlcohol = -1
		for j := 0; j < n; j++ {
			var n string
			var a int
			fmt.Scanf("%s %d", &n, &a)
			if maxAlcohol < a {
				name, maxAlcohol = n, a
			}
		}
		fmt.Println(name)
	}
}
