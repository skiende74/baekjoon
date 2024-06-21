def main():
    string = input().strip()
    bomb = input().strip()
    bombl = list(bomb)
    b_last = bomb[-1]
    bl = len(bomb)
    
    ans = []
    for l in string:
        ans.append(l)
        if b_last == l and bombl == ans[-bl:]:
            del ans[-bl:]

    ans = ''.join(ans) if ans else "FRULA"
    print(ans)

main()