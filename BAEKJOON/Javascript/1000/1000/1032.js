const fs = require("fs")
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n")


const N = parseInt(input.shift())

let ans = []
const cmdLength = input[0].length
for (j = 0; j < cmdLength; j++) {
  let char = input[0][j]
  let flag = true
  for (i = 0; i < N; i++) {
    if (input[i][j] !== char) {
      flag = false
      i = N
    }
  }

  if (flag === true) {
    ans.push(char)
  } else {
    ans.push("?")
  }
}
console.log(ans.join(""))
