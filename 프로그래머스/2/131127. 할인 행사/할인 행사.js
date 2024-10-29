function solution(want, number, discount) {
    let cnt=0;
    for (let i = 0; i<discount.length-9; i++){
        const counter = discount.slice(i,i+10)
        .reduce((prev, cur)=>({...prev, [cur]:(prev[cur]??0)+1}),{});
        if (want.every((w,j)=>counter[w]>=number[j])) cnt += 1;
    }
    return cnt;
}