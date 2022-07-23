const fs = require("fs")
const filepath: string = process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt"
const input: number[] = fs.readFileSync(filepath).toString().trim().split(" ").map((x: string) => parseInt(x))

const [X, Y, W, S] = input
const minVal: number = Math.min(X, Y)
const maxVal: number = Math.max(X, Y)

let dist: number = 0
if (S < W * 2) {
  dist += minVal * S
  if (S < W) {
    dist += Math.floor((maxVal - minVal) / 2) * 2 * S
    dist += ((maxVal - minVal) % 2) * W
  } else {
    dist += (maxVal - minVal) * W
  }
} else {
  dist += (X + Y) * W
}
console.log(dist)
