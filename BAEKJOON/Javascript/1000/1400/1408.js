const fs = require("fs")
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n")

const convertTime = function(strTime) {
  let intTime = 0
  intTime += (parseInt(strTime[0]) * 10 + parseInt(strTime[1])) * 60 * 60
  intTime += (parseInt(strTime[3]) * 10 + parseInt(strTime[4])) * 60
  intTime += (parseInt(strTime[6]) * 10 + parseInt(strTime[7]))
  return intTime
}

let now = convertTime(input[0])
let start = convertTime(input[1])
if (now > start) {
  start += 24 * 60 * 60
}

const diffTime = start - now
answer = `${String(parseInt(diffTime / (60 * 60))).padStart(2, "0")}:${String(parseInt((diffTime % (60 * 60)) / 60)).padStart(2, "0")}:${String(diffTime % 60).padStart(2, "0")}`
console.log(answer)