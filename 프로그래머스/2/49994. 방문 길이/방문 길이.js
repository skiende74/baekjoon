const vert = Array.from({length:11},()=>Array.from({length:11}, ()=>0));
const horz = Array.from({length:11},()=>Array.from({length:11}, ()=>0));
const sum = (arr)=>arr.reduce((prev, el)=>prev+el, 0);
function solution(dirs) {
    let x = 0;
    let y = 0;
    for (let dir of dirs) {
        if (dir === 'U' && y > -5) {
            vert[y+4][x+5] = 1;
            y -= 1;
        }
        else if (dir === 'D' && y < 5) {
            vert[y+5][x+5] = 1;
            y += 1;
        }
        else if (dir === 'L' && x > -5) {
            horz[y+5][x+4] = 1;
            x -= 1;
        }
        else if (dir === 'R' && x < 5) {
            horz[y+5][x+5] = 1;
            x += 1;
        }
        
    }
    return sum(horz.map(sum)) + sum(vert.map(sum))
}