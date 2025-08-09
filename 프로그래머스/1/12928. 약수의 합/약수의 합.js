function solution(n) {
    let ans = 0;
    for (let i = 1; i<=n; i++){
        if (n % i === 0) {
            ans += i;
        }
    }
    return Array.from({length:n},(_,i)=> i+1).filter(num=> n % num === 0).reduce((a,b)=>a+b,0);
    return ans;
}