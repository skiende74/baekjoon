function solution(n)
{
    var ans = 1;
    while(n > 1){
        if(Number.isInteger(n/2)){
            n/=2;
            continue
        }
        n -= 1;
        ans += 1;
      
    }
    return ans;
}