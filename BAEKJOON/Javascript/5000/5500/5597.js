/*
Title : 과제 안 내신 분..?
Link : https://www.acmicpc.net/problem/5597
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

const students = Array.from({ length: 30 }, () => 0);
input.forEach((student) => {
  const index = Number(student) - 1;
  students[index] = 1;
});

const notSubmitted = students.reduce((acc, cur, index) => {
  if (cur === 0) {
    acc.push(index + 1);
  }
  return acc;
}, []);

console.log(notSubmitted.join("\n"));
