function solution(arr, n) {
    if (arr.length%2===0){
        return arr.map((x,i)=>x+n*(i%2));
    }
    return arr.map((x,i)=>x+n*(1-i%2));
}