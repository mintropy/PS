/*
Title : 바구니 뒤집기
Link : https://www.acmicpc.net/problem/10811
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const basket = Array.from({ length: n }, (_, i) => i + 1);

for (let i = 0; i < m; i++) {
  const [start, end] = input[i + 1].split(" ").map(Number);
  const temp = basket.slice(start - 1, end).reverse();
  basket.splice(start - 1, end - start + 1, ...temp);
}

console.log(basket.join(" "));
