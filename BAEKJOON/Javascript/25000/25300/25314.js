/*
Title : 코딩은 체육과목 입니다
Link : https://www.acmicpc.net/problem/25314
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const N = parseInt(fs.readFileSync(filepath).toString().trim());

let output = "long";
for (let i = 2; i * 4 <= N; i++) {
  output += " long";
}
output += " int";

console.log(output);
