const input = ()=>require('fs').readFileSync('/dev/stdin').toString().trim();
const [a, b]= input().split(' ').map(num=>parseInt(num));
console.log(a/b);