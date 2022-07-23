const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim()

const [a, d, k] = input.split(" ").map(x => parseInt(x))
const diff = k - a
const q = diff / d
const r = diff % d

if (r !== 0 || q < 0) {
  console.log("X")
} else {
  console.log(q + 1)
}