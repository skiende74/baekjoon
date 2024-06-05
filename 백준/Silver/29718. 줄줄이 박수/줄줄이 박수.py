N, M = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
A = int(input())

def col_sum(j):
    return sum([row[j] for row in grid])
val = sum([col_sum(i) for i in range(A)])
max_val = val
for i in range(A, M):
    val += col_sum(i) - col_sum(i-A)
    max_val = max(max_val, val)
print(max_val)