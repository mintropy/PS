package main

import "fmt"

func main() {
	var plain [101][101]bool
	for i := 0; i < 4; i++ {
		var x1, y1, x2, y2 int
		fmt.Scanln(&x1, &y1, &x2, &y2)
		for x := x1; x < x2; x++ {
			for y := y1; y < y2; y++ {
				plain[x][y] = true
			}
		}
	}
	ans := 0
	for i := 1; i <= 100; i++ {
		for j := 1; j <= 100; j++ {
			if plain[i][j] {
				ans++
			}
		}
	}
	fmt.Print(ans)
}
