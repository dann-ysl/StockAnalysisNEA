from sortSearch import *
stock = [["AAPL", 25, 0.86],
        ["TSLA", 51, 2.6], 
        ["MSFT", 13.2, 1.2]]

stockLBUB = [[23,100],[2,4]]

closeLB = 23
closeUB = 100
voltLB = 2
voltUB = 4

#sortA = sortedArray(stock, 1)
#sortB = sortedArray(stock, 2)

def search(arr, filterArr):

    for i in range(len(filterArr)):
        length = len(arr)
        sortArr = sortedArray(arr, (i+1))
        
        valueArr = [0 for x in range(length)]
        for j in range(length):
            valueArr[j] = sortArr[j][i+1]

        indexArr = linearSearchRange(valueArr, filterArr[i][0], filterArr[i][1])
        arr = sortArr[indexArr[0]:(indexArr[1]+1)]
    
    return arr

def linearSearchRange(arr, lb, ub):

    output = [0,0]
    length = len(arr)
    leftCounter = 0
    leftCheck = False
    rightCounter = length - 1
    rightCheck = False

    while leftCheck == False:
        if lb <= arr[leftCounter]:
            output[0] =  leftCounter
            leftCheck = True
        else:
            leftCounter += 1

    while rightCheck == False:
        if ub >= arr[rightCounter]:
            output[1] = rightCounter
            rightCheck = True
        else:
            rightCounter += -1
    
    return output


print(search(stock, stockLBUB))

