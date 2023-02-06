/*
Title : 창업
Link : https://www.acmicpc.net/problem/16890
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

let ko_alp = [];
let cu_alp = [];

for (let i = 0; i < input[0].length; i++) {
  ko_alp.push(input[0][i]);
  cu_alp.push(input[1][i]);
}
const L = ko_alp.length;

ko_alp.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0));
cu_alp.sort((a, b) => b.charCodeAt(0) - a.charCodeAt(0));

let ko = [];
let cu = [];
for (let i = 0; i < parseInt(L / 2); i++) {
  ko.push(ko_alp[i]);
  cu.push(cu_alp[i]);
}
if (L % 2 === 1) {
  ko.push(ko_alp[L - parseInt(L / 2)]);
}

let ans = new Array(L);
let [lIdx, rIdx] = [0, L - 1];

for (let t = 0; t < L - 1; t++) {}

let tmp = "";
console.log();
