function solution(A,B){
    A.sort((a,b)=>a-b);
    B.sort((a,b)=>a-b);
    B.reverse();
    
    return A.reduce((prev, a, i)=>prev+a*B[i],0);
}