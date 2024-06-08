seq = input()
N = len(seq)

def func(X_str):
    global is_possible
    n = len(X_str)
    if n==0: return ''
    q,r = divmod(n, 4)
    q2,r2 = divmod(r,2)
    if r2!=0: is_possible = False
    return 'AAAA'*q+'BB'*q2

is_possible= True
res = []
for x_str in seq.split('.'):
    res.append(func(x_str))

print('.'.join(res) if is_possible else '-1')