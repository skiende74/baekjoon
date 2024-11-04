class PQ {
    constructor() {
        this.queue = [0];
    }

    enqueue(el) {
        let i = this.queue.length;
        while (i > 1 && this.queue[Math.floor(i / 2)] > el) {
            this.queue[i] = this.queue[Math.floor(i / 2)];
            i = Math.floor(i / 2);
        }
        this.queue[i] = el;
    }

    dequeue() {
        if (this.size() === 0) return null;

        const result = this.queue[1];
        
        // 큐에 노드가 하나만 남은 경우: 단순히 pop() 반환하고 종료
        if (this.size() === 1) { 
            this.queue.pop();
            return result;
        }

        // 루트에 마지막 값을 넣고 힙 재정렬 시작
        this.queue[1] = this.queue.pop();

        let [pIdx, cIdx] = [1, 2];
        while (cIdx < this.queue.length) {
            // 오른쪽 자식이 존재하고, 오른쪽 자식이 더 작으면 cIdx를 오른쪽 자식으로 이동
            if (cIdx + 1 < this.queue.length && this.queue[cIdx] > this.queue[cIdx + 1]) {
                cIdx += 1;
            }
            
            // 부모가 자식보다 작거나 같으면 힙 조건을 만족하므로 종료
            if (this.queue[pIdx] <= this.queue[cIdx]) break;

            // 부모와 자식을 교환하고 인덱스를 업데이트
            [this.queue[pIdx], this.queue[cIdx]] = [this.queue[cIdx], this.queue[pIdx]];
            [pIdx, cIdx] = [cIdx, cIdx * 2];
        }
        
        return result;
    }

    size() {
        return this.queue.length - 1;
    }

    front() {
        return this.queue[1] ?? null;
    }
}

function solution(scoville, K) {
    const pq = new PQ();
    for (const s of scoville) pq.enqueue(s);
    
    let cnt = 0;

    while (pq.size() > 1 && pq.front() < K) {
        const [a, b] = [pq.dequeue(), pq.dequeue()];
        pq.enqueue(a + b * 2);
        cnt += 1;
    }
    return pq.front() >= K ? cnt : -1;
}
