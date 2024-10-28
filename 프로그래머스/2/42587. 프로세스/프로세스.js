function solution(priorities, location) {
    let cnt = 0;
    let maxIdx = -1;
    while (maxIdx !== location) {
    const M = Math.max(...priorities);
    maxIdx = priorities.findIndex(el=>el===M);
    priorities = [...priorities.slice(maxIdx+1),...priorities.slice(0,maxIdx)];
    cnt += 1;
    }
    return cnt;
}