function solution(s) {
    const seq = s.split(' ').map(Number);
    return `${Math.min(...seq)} ${Math.max(...seq)}`;
}