const inputs = require('fs').readFileSync('/dev/stdin').toString().split('\n').map(num=>parseInt(num));

let maxVal = -1;
let maxIdx = -1;
for (let i=0;i<9;i++) {
    const num = inputs[i];
    if (maxVal < num){
        maxIdx = i;
        maxVal = num;
    }
}
console.log(maxVal)
console.log(maxIdx+1);