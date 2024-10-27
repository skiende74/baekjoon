function solution(s){
    let counter = 0;
    for (let i=0;i<s.length;i++){
        if(s[i] === '(') counter += 1;
        else if(counter === 0) return false;
        else counter -= 1;
    }
    return counter===0;
}