const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim().split("\n")

const N = parseInt(input[0])
let dasom = parseInt(input[1])
let votes = Array(101).fill(0)

for (let i = 0; i < N - 1; i++) {
  v = parseInt(input[i + 2])
  votes[v]++
}

let answer = 0
for (let i = 100; i > 0; i--) {
  if (votes[i] === 0) {
    continue
  }
  while (votes[i] > 0) {
    if (dasom > i) {
      break
    }
    dasom++
    votes[i]--
    votes[i - 1]++
    answer++
  }
  if ((votes[i] !== 0 && dasom >= i) || dasom > i) {
    break
  }
}
console.log(answer)
