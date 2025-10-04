/*
Title : 문자와 문자열
Link : https://www.acmicpc.net/problem/27866
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim();

const S = input.split("\n")[0];
const i = Number(input.split("\n")[1]) - 1;
const result = S[i];
console.log(result);
