seq = input()
N = len(seq)
cnt = 0
ans = []
stack = ''
for i, c in enumerate(seq):
    if c == '<': 
        cnt += 1
        if stack:
            ans.append(stack[::-1])
            stack = ''
        stack += '<'
    elif c == '>':
        cnt -= 1
        ans.append(stack+'>')
        stack = ''
    elif c == ' ':
        if cnt == 0:
            ans.append(stack[::-1])
            stack = ''
        else:
            stack += ' '
    else:  
        stack += c
if stack: ans.append(stack[::-1])

prev_is_tag = True
answer = ''
for l in ans:
    is_tag = l[0] == '<' and l[-1] == '>'
    if not prev_is_tag and not is_tag:
        l = ' '+l
    answer += l
    prev_is_tag = is_tag
print(answer)    