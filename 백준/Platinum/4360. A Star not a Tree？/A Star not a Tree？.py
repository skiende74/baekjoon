N = int(input())
nodes = [list(map(int,input().split())) for _ in range(N)]

xs = [x for x,y in nodes]
ys = [y for x,y in nodes]

x,y = 0, 0
def round(num):
    rem = num-int(num)
    return int(num) + (1 if rem>=0.5 else 0)


def r2(x,y,xi,yi):
    return (x-xi)**2 + (y-yi)**2

# L = sum((x-xi)**2 + (y-yi)**2)**0.5
# dL = 0.5*((x-xi)**2 + (y-yi)**2)**(-0.5) * (2*(x-xi) + 2*(y-yi))

# dx = ((x-xi)**2 + (y-yi)**2)**(-0.5) * (x-xi)

def suppress(x, h):
    if abs(x)<h: return x
    return x/abs(x)*h

for _ in range(2*10**4):
    dx,dy = 0,0
    
    for i in range(N):
        r = r2(x,y,xs[i],ys[i])
        if r == 0: continue
        val = r**(-.5)
        dx -= val*(x-xs[i])
        dy -= val*(y-ys[i])
    x += suppress(dx, 1) * 1
    y += suppress(dy, 1) * 1
#print(x,y)
print(round(sum([ ((x-xi)**2 + (y-yi)**2)**0.5 for xi,yi in nodes])))