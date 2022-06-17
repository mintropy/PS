package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var wr = bufio.NewWriter(os.Stdout)

func nextInt() int {
	sc.Scan()
	text := sc.Text()
	v, _ := strconv.Atoi(text)
	return v
}

func nextWord() string {
	sc.Scan()
	return sc.Text()
}

func main() {
    sc.Split(bufio.ScanWords)
    defer wr.Flush()

    N := nextInt()
	commands := make([]string, N)
	for i := 0; i < N; i++ {
		commands[i] = nextWord()
	}
	cmdLength := len(commands[0])

	answer := make([]bool, cmdLength)
	for j := 0; j < cmdLength; j++ {
		char := commands[0][j]
		flag := true
		for i := 1; i < N; i++ {
			if commands[i][j] != char {
				flag = false
				break
			}
		}
		answer[j] = flag
	}
    for j, b := range answer {
        if b {
            fmt.Fprint(wr, string(commands[0][j]))
        } else {
            fmt.Fprint(wr, "?")
        }
    }
}
