N,M = map(int,input().split())
cards = sorted(map(int,input().split()))
maxNum = -1

def updateMaxNum(i,j,k,maxNum):
    cardSum=cards[i]+cards[j]+cards[k]
    if cardSum<=M and cardSum>maxNum:
        return cardSum
    else:
        return maxNum

numberOfCards=len(cards)

for i in range(numberOfCards-2):
    for j in range(i+1,numberOfCards-1):
        for k in range(j+1,numberOfCards):
            maxNum=updateMaxNum(i,j,k,maxNum)

print(maxNum)