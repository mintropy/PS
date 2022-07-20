const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim().split("\n")

const N = parseInt(input[0])
let ans = 0
const seq = input[1].split(" ").map(x => parseInt(x))
for (var k in seq) {
  if (seq[k] === N) {
    ans++
  }
}
console.log(ans)
