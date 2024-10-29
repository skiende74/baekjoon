function solution(n,a,b)
{
    let cnt = 0;
    while (a !== b){
    a = Math.floor((a+1)/2);
    b = Math.floor((b+1)/2);
    cnt += 1;
    }
    return cnt;
}