function solution(ingredient) {
    let result = 0;    

    const stack = [];
    for (const item of ingredient){
        stack.push(item);
        if ( item == 1 && stack.length >=4){
            if (stack.slice(-4).join(' ') === '1 2 3 1'){
                stack.pop();
                stack.pop();
                stack.pop();
                stack.pop();
                result += 1;
            }            
        }
    }
    return result;
}