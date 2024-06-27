def solution(A, B):
    A.sort()
    B.sort()
    score = 0
    j = 0

    for a in A:
        while j < len(B) and B[j] <= a:
            j += 1
        if j < len(B):
            score += 1
            j += 1

    return score