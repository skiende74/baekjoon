function solution(elements) {
    const n = elements.length;
    const res = new Set();
    for (let i = 0; i<n; i++){
        let total = 0;
        for (let j=i; j<i+n; j++){
            total += elements[j%n];
            res.add(total);
        }
    }
    return res.size
}