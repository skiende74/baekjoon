const pair = {')':'(', '}':'{',']':'['};

const isVPS = (str)=> {
    const stack = [];
    for (let i =0; i<str.length;i++){
        const el = str[i];
        if ('([{'.includes(el)){
            stack.push(el);
            continue;
        }
        if (stack.length>0 && pair[el]===stack[stack.length-1]) stack.pop();
        else return false;            
    }
    return stack.length === 0;
}

function solution(s) {
    return Array.from({length:s.length},(_,i)=>i).map(i=>isVPS(s.slice(i)+s.slice(0,i))?1:0).reduce((prev,el)=>prev+el,0)
}