function solution(money) {
    const cup = Math.floor(money/5500);
    const remains = money - cup*5500;
    return [cup, remains]
}