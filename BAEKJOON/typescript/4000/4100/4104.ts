const fs = require("fs")
const filepath: string = process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt"
const input: string[] = fs.readFileSync(filepath).toString().trim().split("\n")

const len: number = input.length
for (let i = 0; i < len - 1; i++) {
  let line: string = input[i]
  const [x, y]: number[]= line.split(" ").map((x: string) => parseInt(x))
  if (x === 0 && y === 0) {
    break
  }
  if (x > y) {
    console.log("Yes")
  } else {
    console.log("No")
  }
}