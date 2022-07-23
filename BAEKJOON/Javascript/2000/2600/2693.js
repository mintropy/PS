const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim().split("\n")

const N = parseInt(input[0])
for (let i = 1; i <= N; i++) {
  let seq = input[i].split(" ").map(x => parseInt(x))
  seq.sort(function(x, y){return x - y})
  console.log(seq[7])
}
