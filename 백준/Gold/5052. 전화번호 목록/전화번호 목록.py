import sys
input = lambda: sys.stdin.readline().rstrip()
class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None]*10
def add(word):
    t = root
    for w in word:
        index = int(w)
        if t.children[index] is None: t.children[index] = TrieNode()
        t = t.children[index]
    t.is_end = True
def search(word):
    t = root
    for w in word:
        if t.is_end: return True
        index = int(w)
        t = t.children[index]
    return False
T = int(input())
for _ in range(T):
    N = int(input())
    words = [input() for _ in range(N)]

    root = TrieNode()
    for word in words:
        add(word)
    exist = False
    for word in words:
        if search(word): exist = True
    print('NO' if exist else 'YES')