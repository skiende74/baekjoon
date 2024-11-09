function solution(answers) {
const ans1 = [1,2,3,4,5]
const ans2 = [2,1,2,3,2,4,2,5];
const ans3 = [3,3,1,1,2,2,4,4,5,5];
    const N = answers.length;
    const cnt1 = Array.from({length:N}, (_,i)=>ans1[i%ans1.length]).reduce((prev,el,i)=>prev+(el===answers[i]?1:0),0);
    const cnt2 = Array.from({length:N}, (_,i)=>ans2[i%ans2.length]).reduce((prev,el,i)=>prev+(el===answers[i]?1:0),0);
    const cnt3 = Array.from({length:N}, (_,i)=>ans3[i%ans3.length]).reduce((prev,el,i)=>prev+(el===answers[i]?1:0),0);
    
    const maxCnt = Math.max(cnt1,cnt2,cnt3);
    //
    return [cnt1, cnt2,cnt3].map((el,i)=>[el,i]).filter(el => el[0]===maxCnt).map(([el,i])=>i+1);
}