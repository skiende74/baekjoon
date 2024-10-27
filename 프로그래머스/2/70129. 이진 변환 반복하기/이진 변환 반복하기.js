let cnt = 0;
let del = 0;
function solution(s) {
    if (s==='1') return [cnt, del]
    del += Array.from(s.matchAll('0')).length;
    cnt += 1
    s = Array.from(s.matchAll('1')).length.toString(2);
    return solution(s);
}