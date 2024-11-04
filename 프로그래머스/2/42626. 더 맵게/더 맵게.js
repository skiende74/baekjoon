class PQ {
    constructor() {
        this.queue = [0];
    }

    enqueue(element) {
        let insertIdx = this.queue.length;
        while (insertIdx > 1 && this.queue[Math.floor(insertIdx / 2)] > element) {
            this.queue[insertIdx] = this.queue[Math.floor(insertIdx / 2)];
            insertIdx = Math.floor(insertIdx / 2);
        }
        this.queue[insertIdx] = element;
    }

    dequeue() {
        if (this.queue.length <= 1) return null;
        
        const delValue = this.queue[1];
        const lastValue = this.queue.pop();

        if (this.queue.length === 1) return delValue;
        
        this.queue[1] = lastValue;

        let pIdx = 1;
        let cIdx = 2;

        while (cIdx < this.queue.length) {
            if (cIdx + 1 < this.queue.length && this.queue[cIdx] > this.queue[cIdx + 1]) {
                cIdx += 1;
            }
            if (lastValue <= this.queue[cIdx]) break;
            
            this.queue[pIdx] = this.queue[cIdx];
            pIdx = cIdx;
            cIdx *= 2;
        }

        this.queue[pIdx] = lastValue;
        return delValue;
    }

    front() {
        return this.queue[1] || null;
    }

    size() {
        return this.queue.length - 1;
    }

    clear() {
        this.queue = [0];
    }
}

function solution(scoville, K) {
    const pq = new PQ();
    for (const s of scoville) {
        pq.enqueue(s);
    }
    let cnt = 0;
    while (pq.size() > 1 && pq.front() < K) {
        const [a, b] = [pq.dequeue(), pq.dequeue()];
        pq.enqueue(a + b * 2);
        cnt += 1;
    }
    return pq.front() >= K ? cnt : -1;
}
