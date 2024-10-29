const dp = Array.from({length:2001},()=>0)
dp[0] = 1;
dp[1] = 1;
function solution(n) {    
    if (dp[n]) return dp[n];
    dp[n] = (solution(n-1)+solution(n-2))%1234567;
    return dp[n];
}