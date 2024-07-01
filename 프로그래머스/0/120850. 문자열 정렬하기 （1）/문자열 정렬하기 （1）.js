function solution(my_string) {
    return my_string.split('').filter(a=>'0'<=a&&a<='9').map(n=>Number(n)).sort()
}