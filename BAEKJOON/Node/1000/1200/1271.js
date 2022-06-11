const fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ").map(BigInt)
// const input = '1000 100'.split(' ')

let answer = input[0] / input[1] + '\n'
answer += input[0] % input[1]
console.log(answer)
