/*
Title : 공 바꾸기
Link : https://www.acmicpc.net/problem/10813
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const balls = Array.from({ length: n }, (_, i) => i + 1);

for (let i = 1; i <= m; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  const temp = balls[a - 1];
  balls[a - 1] = balls[b - 1];
  balls[b - 1] = temp;
}

console.log(balls.join(" "));
