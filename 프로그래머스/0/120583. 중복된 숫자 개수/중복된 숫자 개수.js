function solution(array, n) {
    let count=0;
    for (let a of array){
        if(a === n)
            count++;
    }
    return count;
}