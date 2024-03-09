string = input()
N = len(string)

ans = N



for i in range(N):
    if i>=1 and string[i-1:i+1] in ['c=','c-','d-','lj','nj','s=','z=']:   
        ans -= 1
    if i>=2 and string[i-2:i+1] == 'dz=':
        ans -= 1

print(ans)