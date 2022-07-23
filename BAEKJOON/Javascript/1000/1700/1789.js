const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim()


const N = parseInt(input)
for (i = 1; true; i++) {
  if (N < parseInt((i + 1) * (i + 2) / 2)) {
    console.log(i)
    break
  }
}
