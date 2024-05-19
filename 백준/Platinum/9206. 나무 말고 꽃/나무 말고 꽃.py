from math import exp, pi


V, N = input().split()
V = float(V)
N = int(N)
queries = [list(map(float,input().split())) for _ in range(N)]

n = 10**5
dh = 1/n
result = []
for a,b,h in queries:
    dh = h/n
    xs = [i*dh for i in range(n+1)]
    f = lambda x: ((a*exp(-x**2)+b*x**0.5)**2)
    ys = [f(x)*pi*4 for x in xs[1:-1:2]]
    ys2 = [f(x)*pi*2 for x in xs[2:-1:2]]
    result.append( (sum(ys)+sum(ys2)+(f(xs[0])*pi+f(xs[-1])*pi))*dh/3 )
#print(result)
result = list(map(lambda x: abs(x-V), result))

print(result.index(min(result)))