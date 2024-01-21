/*
Title : 공 넣기
Link : https://www.acmicpc.net/problem/10810
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const basket = new Array(n).fill(0);
for (let x = 0; x < m; x++) {
  const [i, j, k] = input[x + 1].split(" ").map(Number);
  for (let y = i; y <= j; y++) {
    basket[y - 1] = k;
  }
}
console.log(basket.join(" "));
