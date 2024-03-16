def processInputs():
    M,N = map(int,input().split())
    board=[]
    for i in range(M):
        board.append(list(input()))
    return M,N,board
def findMinCount(board,boardB,boardW):
    M,N = len(board),len(board[0])
    minCount=1000000
    for i in range(0,1+ (M-8)):
        for j in range(0, 1+ (N-8)):
            boardCut=cutBoard(board,i,j)
            minCount = min(minCount, countDifferent(boardCut,boardB), countDifferent(boardCut,boardW))
    return minCount
def countDifferent(A,B):
    M=len(A)
    N=len(A[0])
    count=0
    for i in range(M):
        for j in range(N):
            if A[i][j] != B[i][j]:
                count += 1
    return count
def cutBoard(board,i,j):
    newBoard = [[] for _ in range(8)]
    for row in range(8):
        for col in range(8):
            newBoard[row].append(board[row+i][col+j])
    return newBoard
    
M,N,board = processInputs()
boardB=[ list('BWBWBWBW') if i%2==0 else list('WBWBWBWB') for i in range(8) ]
boardW=[ list('BWBWBWBW') if i%2==1 else list('WBWBWBWB') for i in range(8) ]

print(findMinCount(board,boardB,boardW))