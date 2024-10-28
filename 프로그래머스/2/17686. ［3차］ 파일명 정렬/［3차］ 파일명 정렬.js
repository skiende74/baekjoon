function solution(files) {
    const reg=/([a-zA-Z .-]+)(\d{1,5})(.*)/;
    files.sort((a,b)=>{
        const A = a.toLowerCase().match(reg);
        const B = b.toLowerCase().match(reg);

        return A[1].localeCompare(B[1])!==0? A[1].localeCompare(B[1]): 
         Number(A[2])!==Number(B[2])? Number(A[2])-Number(B[2]):
        A.index-B.index;});
    return files
}