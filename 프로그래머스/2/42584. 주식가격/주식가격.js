function solution(prices) {
    const N = prices.length;
    const answer = Array.from({length:N},()=>0);
    prices[N-1] = -1;
    
    const stack = [[prices[0],0]];
    for (let i=1; i<N; i++){
        while (stack.length>0 && stack.at(-1)[0] > prices[i]){
            const [el, idx] = stack.pop();
            answer[idx] = i-idx;
        }
        stack.push([prices[i],i])//
    }
    return answer;
}