// const fs = require("fs")
// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
const input = `3
0
0
0
10
1
2
4
8
16
32
64
128
256
-512
6
9223372036854775807
9223372036854775806
9223372036854775805
-9223372036854775807
-9223372036854775806
-9223372036854775804
`.split("\n")

let idx = 0

for (let i = 0; i < 3; i++) {
  const testCase = input[idx]
  idx++
  let sum = 0n
  for (let j = 0; j < testCase; j++) {
    sum += BigInt(input[idx])
    idx++ 
  }
  if (sum === 0n) {
    console.log(0)
  } else if (sum > 0n) {
    console.log("+")
  } else {
    console.log("-")
  }
}