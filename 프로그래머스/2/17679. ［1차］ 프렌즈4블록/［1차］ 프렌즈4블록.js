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
        let isFound = false;
        for (let i = 0; i<m-1 ; i++){
            for (let j = 0; j<n-1; j++){
                const c = grid[i][j]
                if (c===' ')continue;
                const i2j2s = [[0,0],[0,1],[1,0],[1,1]]
                               .map(([di,dj])=>[i+di,j+dj]);
                const isExplode = i2j2s
                                  .filter(([i2,j2])=>grid[i2][j2] === grid[i][j]).length === 4;
                if (isExplode) {
                    i2j2s.forEach(([i2,j2])=>{mark[i2][j2] = true});
                    isFound = true;
                }
            }
        }
      

        if (!isFound) break; // 더 이상 지울 2x2 없음

        const next = Array.from({length:m}, ()=>Array(n).fill(' '));
        // 3) 표시된 칸 지우고 개수 세기
        for (let j = 0; j<n; j++){
            let write = m-1;
            for (let i = m-1; i>=0; i--){
                if (!mark[i][j]){
                    next[write][j] = grid[i][j];
                    write -= 1;
                }          
                else{
                    totalRemoved += 1;
                }
            }
        }
        
        for (let i = 0; i<m; i++){
            for (let j = 0; j<n; j++){
                grid[i][j] = next[i][j];
            }
        }
        //return totalRemoved;
  }
 
    
  return totalRemoved;
}
