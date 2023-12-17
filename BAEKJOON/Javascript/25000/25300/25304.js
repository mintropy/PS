/*
Title : 영수증
Link : https://www.acmicpc.net/problem/25304
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

const X = Number(input[0]);
const N = Number(input[1]);
let totalPrice = 0;
for (let i = 0; i < N; i++) {
  const [price, count] = input[i + 2].split(" ").map(Number);
  totalPrice += price * count;
}
console.log(totalPrice === X ? "Yes" : "No");
