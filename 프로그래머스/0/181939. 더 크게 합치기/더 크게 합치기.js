function solution(a, b) {
    return Math.max(b*10**(`${a}`.length)+a, a*10**(`${b}`.length)+b)
}