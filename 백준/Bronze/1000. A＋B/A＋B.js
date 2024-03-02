const input = ()=>require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');

const [a,b] = input().map(num=>parseInt(num));
console.log(a+b);