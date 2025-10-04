/*
Title : 수학은 비대면강의입니다
Link : https://www.acmicpc.net/problem/19532
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim();

const [a, b, c, d, e, f] = input.split(" ").map(Number);
const x = (c * e - b * f) / (a * e - b * d);
const y = (a * f - c * d) / (a * e - b * d);
console.log(`${parseInt(x)} ${parseInt(y)}`);
