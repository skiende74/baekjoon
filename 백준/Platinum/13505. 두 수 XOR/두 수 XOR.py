class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
root = Trie()
def add(nums):
    t = root
    for num in nums:
        num = 1-num
        if num not in t.children: t.children[num]=Trie()
        t = t.children[num]
    t.is_end = True

def getXOR(nums):
    t = root
    result = []
    for i, num in enumerate(nums):
        if num in t.children:
            result.append(1)
            t=t.children[num]
        elif 1-num not in t.children:
            result.append(0)
        else:
            result.append(0)
            t=t.children[1-num]
    return result 
        

N = int(input())
seq = list(map(int,input().split()))

def get_binary(num):
    res = []
    for i in range(30):
        num, r = divmod(num, 2)
        res.append(r)
    return res[::-1]
def binary_to_num(binary):
    return sum([ 2**(29-i)*b for i, b in enumerate(binary)])
for num in seq:
    add(get_binary(num))
max_val = 0
for num in seq:
    max_val = max(max_val, binary_to_num(getXOR(get_binary(num))))
print(max_val)