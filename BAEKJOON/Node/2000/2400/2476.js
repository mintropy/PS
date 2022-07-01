const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim().split("\n")

const N = parseInt(input[0])
let answer = 0
for (let i = 1; i <= N; i++) {
  let [a, b, c] = input[i].split(" ").map(x => parseInt(x))
  let tmp = 0
  if (a === b && b === c) {
    tmp = 10000 + 1000 * a
  } else if (a === b) {
    tmp = 1000 + 100 * a
  } else if (b === c) {
    tmp = 1000 + 100 * b
  } else if (c === a) {
    tmp = 1000 + 100 * c
  } else {
    tmp = Math.max(a, b, c) * 100
  }
  if (answer < tmp) {
    answer = tmp
  }
}
console.log(answer)