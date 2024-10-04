from collections import deque


def solution(cap, n, deliveries, pickups):
    delis, picks = [], []
    for i in range(n):
        if deliveries[i] > 0: delis.append((i, deliveries[i]))
        if pickups[i] > 0: picks.append((i, pickups[i]))
    
    def solve(delis, cap_go):
        dist = 0
        while delis and cap_go > 0:
            i, d = delis.pop()
            dist = max(dist, i+1)
            if d > cap_go:
                delis.append((i, d-cap_go))
                cap_go = 0
            else: cap_go -= d
        return dist
    
    ans = 0
    while delis or picks:
        cap_go, cap_come = cap, cap
        dist = max(solve(delis, cap_go), solve(picks, cap_come))
        ans += dist
    return ans*2