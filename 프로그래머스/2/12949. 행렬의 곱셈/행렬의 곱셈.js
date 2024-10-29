function solution(arr1, arr2) {
    const [I, K, J] = [arr1.length, arr1[0].length, arr2[0].length]; 
    const arr = Array.from({length:I},()=>Array.from({length:J}, ()=>0))
    for (let k = 0; k<K; k++){
        for (let i = 0; i<I; i++){
            for (let j = 0; j<J; j++){
                arr[i][j] += arr1[i][k] * arr2[k][j];
            }
        }
    }
    return arr;
}