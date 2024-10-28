function solution(n, words) {
    const used = new Set([words[0]]);
    let prev = words[0];
    for (let i=1; i<words.length;i++){ 
        const word = words[i];
        if (used.has(word) || prev[prev.length-1] !== word[0]) return [i%n+1, Math.floor(i/n)+1];
        used.add(word);
        prev = word;
    }
    return [0,0]
}