function solution(str1, str2) {
    const obj1 = makeCounter(str1);
    const obj2 = makeCounter(str2);
    const keys = new Set();
    for (const k of Object.keys(obj1)){
        keys.add(k);
    }
    for (const k of Object.keys(obj2)){
        keys.add(k);
    }
    
    let disjoint = 0;
    let union = 0;
    
    for (const k of Array.from(keys).filter(k=>/[A-Z]{2,2}/.test(k)) ){
        disjoint += Math.min(obj1[k]??0,  obj2[k]??0);
        union += Math.max(obj1[k]??0, obj2[k]??0);
    }
    if (union === 0) return 65536
    return parseInt((disjoint/union)*65536)
}

function makeCounter(str){
    const counter = {};
    for (let i = 0; i<str.length-1; i++){
        const ch = str.slice(i, i+2).toUpperCase();
        if (counter[ch])
            counter[ch] += 1;
        else
            counter[ch] = 1;
    }
    return counter;
}