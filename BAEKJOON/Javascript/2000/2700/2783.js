// const fs = require('fs')
// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
const input = `3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100`.split('\n')

const [N, M] = input.shift().split(" ").map(Number)

const seq = Array.from(Array(N), () => Array(M).fill(0))
for (let k = 0; k < 2; k ++) {
  for (let i = 0; i < N; i ++) {
    tmp = input.shift().split(" ").map(Number)
    for (let j = 0; j < M; j ++) {
      seq[i][j] += tmp[j]
    }
  }
}

let output = ""
for (let i = 0; i < N; i ++) {
  for (let j = 0; j < M; j ++) {
    output += seq[i][j] + " "
  }
  output += "\n"
}
console.log(output)