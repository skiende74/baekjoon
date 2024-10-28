function solution(s)
{
    const arr = [];
    for (let el of s) {
        if (arr.length > 0 && arr[arr.length-1] === el){
            arr.pop();
            continue;
        }
        arr.push(el);
    }

    return arr.length === 0? 1:0;
}