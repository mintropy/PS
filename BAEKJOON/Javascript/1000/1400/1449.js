/*
Title : 수리공 항승
Link : https://www.acmicpc.net/problem/1449
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

const [N, L] = input[0].split(" ");
const positions = input[1]
  .split(" ")
  .map((x) => parseInt(x))
  .sort(function (a, b) {
    return a - b;
  });
positions.push(5000);

let count = 0;
pos = positions[0];
for (const x of positions) {
  if (x - pos >= L) {
    count += 1;
    pos = x;
  }
}
console.log(count);
