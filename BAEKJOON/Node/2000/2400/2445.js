const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim()

const N = parseInt(input)
let output = ""

for (let i = 1; i <= N; i++) {
  for (let j = 0; j < i; j++) {
    output += "*"
  }
  for (let j = 0; j < N - i; j++) {
    output += " "
  }
  for (let j = 0; j < N - i; j++) {
    output += " "
  }
  for (let j = 0; j < i; j++) {
    output += "*"
  }
  output += "\n"
}
for (let i = N - 1; i > 0; i--) {
  for (let j = 0; j < i; j++) {
    output += "*"
  }
  for (let j = 0; j < N - i; j++) {
    output += " "
  }
  for (let j = 0; j < N - i; j++) {
    output += " "
  }
  for (let j = 0; j < i; j++) {
    output += "*"
  }
  output += "\n"
}
console.log(output)
