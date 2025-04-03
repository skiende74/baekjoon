
function cum(cum_sum, i,j,k){
    return cum_sum[i+k-1][j+k-1] - cum_sum[i-1][j+k-1] - cum_sum[i+k-1][j-1] + cum_sum[i-1][j-1];
}

function solution(board)
{
    const M = board.length;
    const N = board[0].length;
    const cum_sum = [Array.from({length:N+1},()=>0)
                    , ...Array.from({length:M}, (_1, i)=>
                        [0, ...Array.from({length:N}, (_2, j)=>
                         board[i][j])])]; 

    for (let i=1; i<=M; i++){
        for (let j=1; j<=N; j++){
            cum_sum[i][j] = cum_sum[i][j-1] + cum_sum[i-1][j] - cum_sum[i-1][j-1] + board[i-1][j-1];
        }
    }
    
    let k = 0;
    for (let i=1; i<=M; i++){
        for (let j=1; j<=N; j++){
            while (k<=Math.min(N,M) 
                   && i+k-1<=M && j+k-1<=N 
                   && cum(cum_sum, i, j, k) === k**2) k+=1;
        }
    }
    
    return (k-1)**2
}