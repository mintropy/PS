const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

let plain = Array.from(Array(101), () => Array(101).fill(false));
for (let i = 0; i < 4; i++) {
  const [x1, y1, x2, y2] = input[i].split(" ").map((x) => parseInt(x));
  for (let x = x1; x < x2; x++) {
    for (let y = y1; y < y2; y++) {
      plain[x][y] = true;
    }
  }
}
let ans = 0;
for (let i = 1; i <= 100; i++) {
  for (let j = 1; j <= 100; j++) {
    if (plain[i][j]) {
      ans++;
    }
  }
}
console.log(ans);
