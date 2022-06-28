const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim().split("\n")

const N = parseInt(input[0])
const F = parseInt(input[1])

const _N = parseInt(N / 100) * 100

if (_N % F) {
  const ans = String(_N + (F - _N % F))
  const l = ans.length
  console.log(ans.slice(l-2))
} else {
  console.log("00")
}
