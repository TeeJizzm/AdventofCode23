/* ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## */

// Day 01

// -----------------------------------

package main

// Imports
import (
	// Input/Output
	"fmt"
	"os"

	// String manipulation
	"strconv"
	"strings"
	// Other required imports
)

/* -----------------------------------
// Functions */

func find_digits_in_string(line string) ([]int, []int) {

	var digits []int
	var indices []int

	for i, char := range line {
		if val, err := strconv.Atoi(string(char)); err == nil {
			//fmt.Printf("%q looks like a number.\n", val)
			indices = append(indices, i)
			digits = append(digits, val)
		}
	}
	return indices, digits
}

func part_one(lines []string) int {
	var total int = 0

	for _, line := range lines {

		_, digits := find_digits_in_string(line)
		total += (digits[0] * 10) + digits[len(digits)-1]
	}

	return total
}

func part_two(lines []string) int {
	var part2 int = 0

	return part2
}

func main() {
	fmt.Println("Day 01 - Trebuchet?!")

	// ------------ File -------------

	/*/ - File switch
	file, err := os.ReadFile("day01/inc/ex1.txt")
	//file, err := os.ReadFile("day01/inc/ex2.txt")
	/*/ //
	file, err := os.ReadFile("day01/inc/in.txt")
	// --- End --- */

	if err != nil {
		fmt.Println(err)
	}

	text := string(file)
	//fmt.Print(text)

	// ----------- Setup -------------
	lines := strings.Split(text, "\n")

	part1 := part_one(lines)
	part2 := part_two(lines)

	// ----------- Output ------------

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}

// -----------------------------------
