function solution(priorities, location) {
    let cnt = 0;
    let pp = priorities.map((el,idx)=>[el,idx]);
    let pop = [-1,-1];
    while (pop[1] !== location) {
        const M = Math.max(...pp.map(x=>x[0]));
        const maxIdx = pp.findIndex(el=>el[0]===M);
        pop = pp[maxIdx];
        pp = [...pp.slice(maxIdx+1), ...pp.slice(0,maxIdx)];
        
        cnt += 1;
    }
    return cnt;
}