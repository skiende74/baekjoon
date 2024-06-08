int(input())
M = int(input())
seq = set(map(int,input().split()))
seq = list(sorted(seq))
N = len(seq)
seq2 = []
prev = seq[0]
for s in seq[1:]:
    seq2.append(s - prev)
    prev = s
seq2.sort()
# 9간격 -> 5개선택 = 4개지우기
# N-1개에서. M-1개를 지울수있음 -> N-M 개를 고르는 것
 
#  2 3 1 2
# 1 3 6 7 9


# print(seq2)
print(sum(seq2[:N-M]))