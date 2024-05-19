/*
Title : 그림
Link : https://www.acmicpc.net/problem/1926
*/

const fs = require("fs");
const filepath =
  process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
const input = fs.readFileSync(filepath).toString().trim().split("\n");

class BFS {
  constructor(board, n, m) {
    this.board = board;
    this.n = n;
    this.m = m;
    this.visited = Array.from({ length: n + 2 }, () =>
      Array(m + 2).fill(false)
    );
    this.delta = [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ];
    this.pieces = 0;
    this.maxSize = 0;
  }

  search() {
    for (let i = 1; i <= this.n; i++) {
      for (let j = 1; j <= this.m; j++) {
        if (this.board[i][j] === 1 && !this.visited[i][j]) {
          this.bfs(i, j);
          this.pieces++;
        }
      }
    }
    console.log(this.pieces);
    console.log(this.maxSize);
  }

  bfs(i, j) {
    let size = 0;
    this.visited[i][j] = true;
    let queue = [[i, j]];

    while (queue.length) {
      const [x, y] = queue.pop();
      size++;

      for (let i = 0; i < 4; i++) {
        const nx = x + this.delta[i][0];
        const ny = y + this.delta[i][1];

        if (this.board[nx][ny] === 1 && !this.visited[nx][ny]) {
          this.visited[nx][ny] = true;
          queue.push([nx, ny]);
        }
      }
    }
    this.maxSize = Math.max(this.maxSize, size);
  }
}

const [n, m] = input[0].split(" ").map(Number);
let board = Array.from({ length: n + 2 }, () => Array(m + 2).fill(0));
for (let i = 1; i <= n; i++) {
  board[i] = [0].concat(input[i].split(" ").map(Number)).concat([0]);
}

const bfs = new BFS(board, n, m);
bfs.search();
