const gcd = (a, b) => b===0? a: gcd(b, a%b);
const lcm = (a, b) => a*b/gcd(a, b);
function solution(arr) {
    let l = 1;
    for (let el of arr) {
        l = lcm(Math.max(el,l), Math.min(el,l));
    }
    return l;
}