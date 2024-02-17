/*
Title : 최댓값
Link : https://www.acmicpc.net/problem/2566
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs
  .readFileSync(filepath)
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map((x) => +x));

let column = 0;
let row = 0;
let max = -1;

for (let i = 0; i < 9; i++) {
  const maxInRow = Math.max(...input[i]);
  if (maxInRow > max) {
    max = maxInRow;
    column = i + 1;
    row = input[i].indexOf(maxInRow) + 1;
  }
}
console.log(`${max}
${column} ${row}`);
