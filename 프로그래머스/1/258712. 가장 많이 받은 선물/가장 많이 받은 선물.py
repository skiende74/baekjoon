from collections import defaultdict
def solution(friends, gifts):
    given = defaultdict(lambda: 0)
    scores = defaultdict(lambda: 0)
    for gift in gifts:
        given[tuple(gift.split())] += 1
        scores[gift.split()[0]] += 1
        scores[gift.split()[1]] -= 1
    
    N = len(friends)
    get = [0]*N
    for i in range(N):
        for j in range(i+1, N):
            if given[friends[i],friends[j]] > given[friends[j],friends[i]]:
                get[i] += 1
            elif given[friends[i],friends[j]] < given[friends[j],friends[i]]:
                get[j] += 1
            elif scores[friends[i]] > scores[friends[j]]: get[i] += 1
            elif scores[friends[j]] > scores[friends[i]]: get[j] += 1
    print(get)
    return max(get)