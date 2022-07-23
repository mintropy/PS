const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filepath).toString().trim()

let seq = input.split(" ").map(x => parseInt(x)).sort(function(x, y){return x - y})
console.log(seq.join(" "))