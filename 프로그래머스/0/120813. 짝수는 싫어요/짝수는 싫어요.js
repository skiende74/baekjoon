function solution(n) {
    return Array.from({length:n}, (_,i)=>i+1).filter(x=>x%2===1);
}