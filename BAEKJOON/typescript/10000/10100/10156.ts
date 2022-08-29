const fs = require("fs")
const filepath: string = process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt"
const input: number[] = fs.readFileSync(filepath).toString().trim().split(" ").map((x: string) => parseInt(x))

const [K, N, M] = input
const tmp: number = K * N - M

if (tmp < 0) {
  console.log(0)
} else {
  console.log(tmp)
}