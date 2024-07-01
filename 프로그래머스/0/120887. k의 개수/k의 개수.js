const count = (string,c)=>string.split('').filter(x=>x===c).length;
function solution(i, j, k) {
    return count(Array.from({length: j-i+1}, (_,idx)=>i+idx).map(n=>n.toString()).join(''), k.toString());
}