/*
Title : 단어 수학
Link : https://www.acmicpc.net/problem/1339
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

const N = parseInt(input[0]);
let alps = new Array(26);
for (let i = 0; i < 26; i++) {
  alps[i] = 0;
}
for (let i = 1; i <= N; i++) {
  for (let j = 0; j < input[i].length; j++) {
    alps[input[i].charCodeAt(j) - 65] += 10 ** (input[i].length - j);
  }
}
let tmp = [];
for (let i = 0; i < 26; i++) {
  tmp.push([alps[i], i]);
}
tmp.sort((x, y) => {
  x[0] - y[0];
});
let alpToNum = new Array(26);
for (let i = 0; i < 10; i++) {
  alpToNum[tmp[i][1]] = 9 - i;
}

console.log(alpToNum)

let ans = 0;
for (let i = 1; i <= N; i++) {
  let p = 0;
  for (let j = 0; j <= input[i].length; j++) {
    p *= 10;
    p += alpToNum[input[i].charCodeAt(j)];
  }
  ans += p;
}
console.log(ans);
