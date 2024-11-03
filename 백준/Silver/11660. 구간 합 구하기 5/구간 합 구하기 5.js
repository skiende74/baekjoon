const lines = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim() // 여기서 문자열 끝의 공백 제거
  .split("\n");

const [N, M] = lines[0].split(" ").map(Number);

// 누적합을 위한 grid 초기화, 입력 데이터는 1부터 시작
const grid = lines.slice(1, N + 1).map(line => [0, ...line.split(" ").map(Number)]);
grid.unshift(Array.from({ length: N + 1 }, () => 0));

// 명령어 목록
const commands = lines.slice(N + 1).map(line => line.split(" ").map(Number));

// 누적합 배열 p_sum 초기화
const p_sum = Array.from({ length: N + 1 }, () => Array(N + 1).fill(0));

// 누적합 계산
for (let i = 1; i <= N; i++) {
  for (let j = 1; j <= N; j++) {
    p_sum[i][j] = p_sum[i][j - 1] + p_sum[i - 1][j] - p_sum[i - 1][j - 1] + grid[i][j];
  }
}

// 쿼리 처리 및 결과 저장
const res = commands
  .map(([i1, j1, i2, j2]) => 
    p_sum[i2][j2] - p_sum[i1 - 1][j2] - p_sum[i2][j1 - 1] + p_sum[i1 - 1][j1 - 1]
  )
  .join("\n");

console.log(res);
