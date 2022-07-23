const fs = require("fs")
const filepath = process.platform === "linux" ? "/dev/stdin" : __dirname+"/input.txt"
const input = fs.readFileSync(filepath).toString().trim().split("\n")


var triangularNumbers = [1]
for (i = 2; triangularNumbers[i - 2] < 1000; i++) {
  triangularNumbers.push(triangularNumbers[i - 2] + i)
}

var isTriangluarNumber = Array.apply(false, Array(1001))
for (var x of triangularNumbers) {
  for (var y of triangularNumbers) {
    for (var z of triangularNumbers) {
      if (x + y + z <= 1000) {
        isTriangluarNumber[x + y + z] = true
      }
    } 
  }
}

for (i = 0; i < parseInt(input[0]); i++) {
  k = parseInt(input[i + 1])
  if (isTriangluarNumber[k]) {
    console.log(1)
  } else {
    console.log(0)
  }
}
