class Line:
    def __init__(self, a, b):
        self.a, self.b = a, b

def cross(l, r):
    # l과 r의 교차점을 반환
    return (r.b - l.b) / (l.a - r.a)

def add_line(a, b):
    l = Line(a, b)
    while len(lines) >= 2 and cross(lines[-2], lines[-1]) >= cross(lines[-1], l):
        lines.pop()
    lines.append(l)

def query(x):
    l, r = 0, len(lines) - 1
    while l < r:
        mid = (l + r) // 2
        if cross(lines[mid], lines[mid + 1]) <= x:
            l = mid + 1
        else:
            r = mid
    a, b = lines[l].a, lines[l].b
    return a * x + b

import sys
input = sys.stdin.readline
data = input().split()
n = int(data[0])
lines = []
qs = list(map(int, input().split()))
a = list(map(int, input().split()))

dp = [0] * n
add_line(a[0], 0)  # 첫 번째 나무의 비용을 0으로 설정

for i in range(1, n):
    dp[i] = query(qs[i])
    add_line(a[i], dp[i])

print(dp[-1])
