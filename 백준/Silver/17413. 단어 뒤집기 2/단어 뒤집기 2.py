seq = input()
N = len(seq)
is_tag = 0
ans = []
stack = ''

x = ''
for i, c in enumerate(seq):
    if c == '<': 
        is_tag = True
        x += stack[::-1] + '<'
        stack = ''
    elif c == '>':
        is_tag = False
        x += stack+'>'
        stack = ''
    elif c == ' ':
        if not is_tag:
            x += stack[::-1] + ' '
            stack = ''
        else:
            stack += ' '
    else:  
        stack += c
x +=  stack[::-1]

print(x)    