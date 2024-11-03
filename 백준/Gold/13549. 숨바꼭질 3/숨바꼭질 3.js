const [S, E] = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .split(" ")
  .map(Number);
const Q = [[S, 0]];
let idx = 0;
const dist = Array(100_001).fill(Infinity);
dist[S] = 0;

while (Q.length > idx) {
  const [i, d] = Q[idx++];

  if (2 * i <= 100_000 && dist[2 * i] > d) {
    dist[2 * i] = d;
    Q[--idx] = [2 * i, d];
  }

  for (let j of [i - 1, i + 1]) {
    if (j < 0 || j > 100_000) continue;
    if (dist[j] <= d + 1) continue;
    dist[j] = d + 1;
    Q.push([j, d + 1]);
  }
}

console.log(dist[E]);
