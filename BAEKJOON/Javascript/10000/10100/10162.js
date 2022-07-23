const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim()


const t = parseInt(input)
if (t % 10 != 0) {
  console.log(-1)
} else {
  const [a, b, c] = [parseInt(t / 300), parseInt((t % 300) / 60), parseInt((t % 60) / 10)]
  console.log(a, b, c)
}
