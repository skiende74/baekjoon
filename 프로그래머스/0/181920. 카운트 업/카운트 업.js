function solution(start_num, end_num) {
    return Array.from({length:end_num-start_num+1}, (v,i)=>i+start_num)
}