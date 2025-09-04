function solution(m, n, board) {
  const g = board.map(r => r.split(''));
  let removed = 0;

  while (true) {
    const mark = Array.from({ length: m }, () => Array(n).fill(false));
    let hit = false;

    // 2x2 탐지 (상수 4칸 비교)
    for (let i = 0; i < m - 1; i++) {
      for (let j = 0; j < n - 1; j++) {
        const c = g[i][j];
        if (!c) continue; // 빈칸이면 스킵
        if (g[i][j+1] === c && g[i+1][j] === c && g[i+1][j+1] === c) {
          mark[i][j] = mark[i][j+1] = mark[i+1][j] = mark[i+1][j+1] = true;
          hit = true;
        }
      }
    }
    if (!hit) break;

    // 지우고 개수 집계
    for (let i = 0; i < m; i++) {
      for (let j = 0; j < n; j++) {
        if (mark[i][j]) { g[i][j] = null; removed++; }
      }
    }

    // next로 낙하(열별 아래부터 채우기)
    const next = Array.from({ length: m }, () => Array(n).fill(null));
    for (let j = 0; j < n; j++) {
      let w = m - 1;
      for (let i = m - 1; i >= 0; i--) {
        if (g[i][j] != null) next[w--][j] = g[i][j];
      }
    }
    // 스왑(얕은 복사)
    for (let i = 0; i < m; i++) g[i] = next[i];
  }

  return removed;
}
