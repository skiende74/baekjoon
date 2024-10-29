function solution(k, tangerine) {
    const counter = {};
    for (let tan of tangerine){
        if (counter[tan]){
            counter[tan] += 1;
        }
        else{
            counter[tan] = 1;
        }
    }
    const counter2 = Object.entries(counter);
    counter2.sort((a,b)=>b[1]-a[1]);
    let count = 0;
    for (let i =0; i<counter2.length; i++){
        count += counter2[i][1];
        if (count >= k) return i+1;
    }
}