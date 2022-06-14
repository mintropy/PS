package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var now, start string
	fmt.Fscanln(reader, &now)
	fmt.Fscanln(reader, &start)

	var nowSecArr, startSecArr []int

	sliceNow := strings.Split(now, ":")
	for _, num := range sliceNow {
		convertNum, _ := strconv.Atoi(num)
		nowSecArr = append(nowSecArr, convertNum)
	}
	sliceStart := strings.Split(start, ":")
	for _, num := range sliceStart {
		convertNum, _ := strconv.Atoi(num)
		startSecArr = append(startSecArr, convertNum)
	}

	nowSec := nowSecArr[0]*60*60 + nowSecArr[1]*60 + nowSecArr[2]
	startSec := startSecArr[0]*60*60 + startSecArr[1]*60 + startSecArr[2]
	var diffSec int
	if nowSec < startSec {
		diffSec = startSec - nowSec
	} else {
		diffSec = 24*60*60 - (nowSec - startSec)
	}

	intAnsArr := [3]int{int(diffSec / (60 * 60)), int((diffSec % (60 * 60)) / 60), diffSec % 60}
	var strAnsArr []string
	for _, num := range intAnsArr {
		convertStr := strconv.Itoa(num)
		if num <= 9 {
			convertStr = "0" + convertStr
		}
		strAnsArr = append(strAnsArr, convertStr)
	}
	fmt.Fprintln(writer, strings.Join(strAnsArr, ":"))
}
