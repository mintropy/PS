const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim()

const [X, Y, Z] = input.split(" ").map(x => parseInt(x))
if (X === Y && Y === Z) {
  console.log(10000 + 1000 * X)
} else if (X === Y) {
  console.log(1000 + 100 * X)
} else if (Y === Z) {
  console.log(1000 + 100 * Y)
} else if (Z === X) {
  console.log(1000 + 100 * Z)
} else {
  maxValue = Math.max(X, Y, Z)
  console.log(maxValue * 100)
}
