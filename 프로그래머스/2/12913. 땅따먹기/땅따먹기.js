function solution(land) {
    const N = land.length;
    const dp = Array.from({length:N}, ()=>Array.from({length:4}, ()=>-1));
    dp[0] = [...land[0]];

    for (let i=1; i<N; i++){
        for (let j=0; j<4; j++){
            dp[i][j] = Math.max(...dp[i-1].slice(0,j), ...dp[i-1].slice(j+1)) + land[i][j];
        }
    }
    return Math.max(...dp[N-1]);
}