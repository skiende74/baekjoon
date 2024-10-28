function solution(brown, yellow) {
    const wPlusH = brown/2+2;
    const wMultH = yellow + brown;

    const w = wPlusH/2 + ((wPlusH/2)**2-wMultH)**0.5
    const h = wPlusH/2 - ((wPlusH/2)**2-wMultH)**0.5;
    return [w,h]
}