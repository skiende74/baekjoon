function solution(N, road, K) {

    const dist = Array.from({length:N+1},()=>
                            Array.from({length:N+1},()=>Infinity));
    for (const [i,j,d] of road) {
        dist[i][j] = Math.min(dist[i][j], d);
        dist[j][i] = Math.min(dist[j][i], d);
    }
    for (let i=1; i<=N; i++) dist[i][i] = 0;
    
    for (let k=1; k<=N; k++){
    for (let i=1; i<=N; i++){
    for (let j=1; j<=N; j++){
        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
        dist[j][i] = Math.min(dist[j][i], dist[j][k] + dist[k][i]);
    }
    }
    }
    return dist[1].reduce((prev,el)=>prev+(el<=K?1:0), 0);
}