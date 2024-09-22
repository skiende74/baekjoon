from collections import defaultdict
from bisect import bisect_left
from itertools import product

def solution(info, query):
    
    infos = [tuple(e.split()) for e in info]
    queries = [tuple(e for e in q.split() if e!='and') for q in query]
    
    # ['java','backend', 'junior','pizza', 100']
    
    scores = defaultdict(list)
    
    for query in infos:
        for record in product( *tuple(('-',q) for q in query[:-1])):
            scores[record].append(int(query[-1]))
    
    for record in scores:
        scores[record].sort()
    output = []

    for query in queries:
        record, score = query[:-1], int(query[-1])
        output.append(len(scores[record]) - bisect_left(scores[record], score))
    return output