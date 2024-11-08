let rows, cols;
let N;
let cnt = 0;
let diag1, diag2;
function dfs(i){
    if (i=== N) {
        cnt += 1;
        return;
    }
    
    for (let j=0; j<N; j++){
        if (cols[j] || diag1[i+j] || diag2[i+(N-1-j)]) continue;
        cols[j] = true; diag1[i+j] = true; diag2[i+(N-1-j)] = true;
        dfs(i+1);
        [cols[j], diag1[i+j], diag2[i+(N-1-j)]] = [false, false,false];
    }
}

function solution(n) {
    N=n;
    cols = Array.from({length:N}, ()=>false);
    diag1 = Array.from({length:2*N-1}, ()=>false);
    diag2 = Array.from({length:2*N-1}, ()=>false);
    dfs(0)

    return cnt;
}