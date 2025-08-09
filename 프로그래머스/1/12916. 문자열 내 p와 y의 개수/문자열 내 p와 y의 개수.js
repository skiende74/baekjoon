function solution(s){
    const s0 = s.toLowerCase();
    return s0.split('p').length === s0.split('y').length
}