import sys
input = lambda : sys.stdin.readline().rstrip()

class Trie():
    def __init__(self):
        self.is_end = False
        self.children = {}
def add(word):
    t = root
    for w in word:
        if w not in t.children: t.children[w] = Trie()
        t = t.children[w] 
    t.is_end = True
def search(word):
    t = root
    cnt = 0
    for w in word:
        t = t.children[w]
        if len(t.children)>1 or t.is_end: cnt += 1
    return cnt

while True:
    
    try: N = int(input())
    except: break
    root = Trie()
    words = [input() for _ in range(N)]
    for word in words:
        add(word)
    print(f'{sum([search(word) for word in words])/N:.2f}')        