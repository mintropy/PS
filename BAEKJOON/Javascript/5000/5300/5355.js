const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

const t = parseInt(input[0]);
for (let i = 1; i <= t; i++) {
  const line = input[i].trim().split(" ");
  let n = parseFloat(line[0]);
  for (let j = 1; j < line.length; j++) {
    let cmd = line[j];
    if (cmd === "@") {
      n *= 3;
    } else if (cmd === "%") {
      n += 5;
    } else if (cmd === "#") {
      n -= 7;
    }
  }
  console.log(n.toFixed(2));
}
