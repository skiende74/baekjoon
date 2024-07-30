def makePrimeNumbers(maxNumber):
    primeNumbers={i for i in range(2,maxNumber+1)}

    for i in range(2,maxNumber+1):
        if i not in primeNumbers:
            continue
        for j in range(2,(maxNumber+1)//i+2):
            if i*j in primeNumbers:
                primeNumbers.remove(i*j)
    return primeNumbers

def processInputs():
    inputNumbers=[]
    while True:
        N=int(input())
        if N != 0:
            inputNumbers.append(N)
        else:
            break
    return inputNumbers

def calculateCountsOfNumbersWithBertrandsPostulate(inputNumber):
    count=0
    for testCase in range(inputNumber+1,inputNumber*2+1):
        if testCase in primeNumbers:
            count+=1
    return count
primeNumbers = makePrimeNumbers(123456*2)
inputNumbers = processInputs()

for inputNumber in inputNumbers:
    print(calculateCountsOfNumbersWithBertrandsPostulate(inputNumber))