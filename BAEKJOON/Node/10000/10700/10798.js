const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim().split("\n")

let seq = []
for (let i = 0; i < 5; i++) {
  seq.push(input[i])
}
let ans = ""
for (let j = 0; j < 15; j++) {
  for (let i = 0; i < 5; i++) {
    if (seq[i].length > j) {
      ans += seq[i][j]
    }
  }
}
console.log(ans)
