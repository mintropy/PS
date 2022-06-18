const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim().split("\n")


let [A, B] = input[0].split(" ").map(x => parseInt(x))
let C = parseInt(input[1])

C += B
A = A + parseInt(C / 60)
B = C % 60
// A, B = A + parseInt(C / 60), C % 60
A %= 24
console.log(A, B)
