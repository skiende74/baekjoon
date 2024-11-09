let N = 7;
const isPrime = Array.from({length:10**N+1}, ()=>true);
const primes = new Set();
function prime(){
    isPrime[0] = false;
    isPrime[1] = false;
    for (let i=2; i<=10**N;i++) {
        if (!isPrime[i]) continue;
        primes.add(i);
        for (let j=2*i; j<=10**N; j+=i){
            isPrime[j] = false;
        }
    }    
}

const ans = new Set();
const visited = new Set();
const perms = [];
let numbers;
function dfs(i) {
    const num = Number(perms.map(i=>numbers[i]).join(''));
    if (isPrime[num]) ans.add(num)
    if (i === N) {
        return;
    }
    
    for (let j=0; j<N; j++){
        if (visited.has(j)) continue;
        visited.add(j);
        perms.push(j);
        dfs(i+1);
        visited.delete(j)
        perms.pop();
    }
}

function solution(nums) {
    numbers = nums;
    N = nums.length;
    prime();
    dfs(0);
    console.log(ans)
    return ans.size
}
