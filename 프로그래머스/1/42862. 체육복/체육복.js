function solution(n, lost, reserve) {
    let result = n;
    lost.sort((a,b)=>a-b);
    reserve.sort((a,b)=>a-b);
    
    const reserved = new Set(reserve);
    
    
    const inter = new Set()
    for (const l of lost){
        if (reserved.has(l)) inter.add(l);
    }
    
    for (const l of lost){
        if (reserved.has(l)) continue;
        if (reserved.has(l-1) && !inter.has(l-1)) { // 봐준다(빌려서 참석)
            reserved.delete(l-1);
            continue;
        }
        if (reserved.has(l+1) && !inter.has(l+1)){
            reserved.delete(l+1);
            continue;
        }
        
        result -= 1; // 참석못함
    }

    return result;
}