package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var maxCal uint64
	var curCal uint64

	heaps := make([]uint64, 1)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			heaps[len(heaps)-1] = curCal
			heaps = append(heaps, 0)
			curCal = 0
			continue
		}
		lineCal, _ := strconv.ParseUint(line, 10, 64)
		curCal += lineCal
		if curCal > maxCal {
			maxCal = curCal
		}
	}
	sort.SliceStable(heaps, func(i, j int) bool { return heaps[i] < heaps[j] })
	var sum uint64
	for i := len(heaps) - 1; i > len(heaps)-4; i-- {
		sum += heaps[i]
	}
	fmt.Println(sum)
}
