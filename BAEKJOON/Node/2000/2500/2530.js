const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim().split("\n")

const [A, B, C] = input[0].split(" ").map(x => parseInt(x))
const D = parseInt(input[1])

const now = A * 60 * 60 + B * 60 + C
const end = now + D

const H = (parseInt(end / (60 * 60))) % 24
const M = parseInt((end % (60 * 60)) / 60)
const S = end % 60
console.log(H, M, S)
