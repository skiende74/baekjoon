function solution2(m, n, board) {
    const explode = new Set();
    for (let i=0; i<m-1;i++){
        for (let j=0; j<n-1;j++){
            const ds = [[0,0],[0,1],[1,0],[1,1]];
            const box = ds.map(([di,dj])=>[i+di,j+dj]);
            const cnt = box.filter(([i2,j2])=>board[i2][j2]===board[i][j]).length;
            if (cnt===4) box.forEach(([i2,j2])=>explode.add([i2,j2].join(',')));
        }
    }
    console.log(explode)
    return explode;
}

function solution(m, n, board) {
  // 문자 배열로 변환
  const grid = board.map(row => row.split(''));
  let totalRemoved = 0;

  const inRange = (y, x) => y + 1 < m && x + 1 < n;

  while (true) {
    // 1) 지울 칸 표시용 boolean 배열
    const mark = Array.from({ length: m }, () => Array(n).fill(false));
    let found = false;

    // 2) 2x2 같은 블록 찾기
    for (let y = 0; y < m - 1; y++) {
      for (let x = 0; x < n - 1; x++) {
        const c = grid[y][x];
        if (!c) continue; // 이미 빈칸(null)
        if (
          inRange(y, x) &&
          grid[y][x + 1] === c &&
          grid[y + 1][x] === c &&
          grid[y + 1][x + 1] === c
        ) {
          mark[y][x] = mark[y][x + 1] = mark[y + 1][x] = mark[y + 1][x + 1] = true;
          found = true;
        }
      }
    }

    if (!found) break; // 더 이상 지울 2x2 없음

    // 3) 표시된 칸 지우고 개수 세기
    let removedThisRound = 0;
    for (let y = 0; y < m; y++) {
      for (let x = 0; x < n; x++) {
        if (mark[y][x]) {
          grid[y][x] = null;
          removedThisRound++;
        }
      }
    }
    totalRemoved += removedThisRound;

    // 4) 중력: 각 열을 아래로 떨어뜨리기
    for (let x = 0; x < n; x++) {
      // 아래에서 위로 읽어와 non-null만 모아 쌓는다
      let write = m - 1;
      for (let y = m - 1; y >= 0; y--) {
        if (grid[y][x] !== null) {
          grid[write][x] = grid[y][x];
          if (write !== y) grid[y][x] = null;
          write--;
        }
      }
      // 나머지 위쪽은 null로 채우기(이미 되어있지만 안전하게)
      for (let y = write; y >= 0; y--) grid[y][x] = null;
    }
  }

  return totalRemoved;
}
