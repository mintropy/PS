package main

import "fmt"

func main() {
	var K, N, M int
	fmt.Scanf("%d %d %d", &K, &N, &M)
	tmp := K*N - M
	if tmp < 0 {
		fmt.Println(0)
	} else {
		fmt.Println(tmp)
	}
}
