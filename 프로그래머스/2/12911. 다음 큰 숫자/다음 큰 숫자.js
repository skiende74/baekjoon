const countOfOne =  n=> Array.from(n.toString(2).matchAll(1)).length;
function solution(n) {
    const a = countOfOne(n);
    for (let i=n+1; i<=1_000_000; i++)
        if (countOfOne(i) === a) return i;
}