const fs = require("fs")
const filePath = process.platform === "linux" ? "/dev/stdin" : __dirname+"/input.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n") 

const testCase = parseInt(input.shift())
for (let i = 0; i < testCase; i++) {
  let [a, b] = input[i].split(" ").map(x => parseInt(x))
  res = a % 10 === 0 ? 10 : a % 10
  b = b % 4 === 0 ? 4 : b % 4
  for (let i = 2; i <= b; i++) {
    res = (res * a) % 10
    res = res === 0 ? 10 : res
  }
  console.log(res)
}
