function solution(people, limit) {
    people.sort((a,b)=>a-b);
    let cnt = 0;
    let [l,r] = [0, people.length-1];

    while (l <= r){
        if (people[l] + people[r] <= limit){
            l += 1;
        }
        r -= 1;
        cnt += 1;
    }
    return cnt;
}