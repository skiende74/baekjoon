function solution(n, left, right) {
    const arr = Array.from({length:right-left+1},(_, i)=>{
        i += left;
        const j = i%n;
        i = Math.floor(i/n);
        return Math.max(i,j)+1;
    });
    
    return arr;
}