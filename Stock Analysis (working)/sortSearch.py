stockArr = [["MSFT", "MSFT90.png", 1023.32],["AAPL", "AAPL90.png", 342.32],["TSLA","TSLA90.png",420.45]]

def sortRecord(arr, column):
    length = len(arr)
    output = [0 for x in range(length)]
    sortArr = [[0,0] for x in range(length)]

    for i in range(length):#extract values from column
        sortArr[i][0] = i
        sortArr[i][1] = arr[i][column]
    
    sortArr = mergeSortIndex(sortArr)
    for j in range(length):
        index = sortArr[j][0]
        output[j] = arr[index]

    return output
    
def mergeSortIndex(arr):

    length = len(arr)
    if length > 1:
        if length % 2 == 0:
            mid = int(length/2)
        else:
            mid = int((length - 1)/2)

        leftArr = mergeSortIndex(arr[0:mid])
        rightArr = mergeSortIndex(arr[mid:length])

        i = 0
        j = 0
        k = 0

        l = len(leftArr)
        r = len(rightArr)
        output = [0 for x in range(l+r)]

        while (i < l) and (j < r):
            if leftArr[i][1] < rightArr[j][1]:
                output[k] = leftArr[i]
                i += 1
            else:
                output[k] = rightArr[j]
                j += 1
            
            k += 1
        
        while i < l:
            output[k] = leftArr[i]
            i += 1
            k += 1
        
        while j < r:
            output[k] = rightArr[j]
            j += 1
            k += 1

        return output
    
    else:
        return arr

def mergeSort(arr):

    length = len(arr)
    if length > 1:
        if length % 2 == 0:
            mid = int(length/2)
        else:
            mid = int((length - 1)/2)

        leftArr = mergeSort(arr[0:mid])
        rightArr = mergeSort(arr[mid:length])

        i = 0
        j = 0
        k = 0

        l = len(leftArr)
        r = len(rightArr)
        output = [0 for x in range(l+r)]
        while (i < l) and (j < r):
            if leftArr[i] < rightArr[j]:
                output[k] = leftArr[i]
                i += 1
            else:
                output[k] = rightArr[j]
                j += 1
            
            k += 1
        
        while i < l:
            output[k] = leftArr[i]
            i += 1
            k += 1
        
        while j < r:
            output[k] = rightArr[j]
            j += 1
            k += 1

        return output
    
    else:
        return arr

def sortedArray(arr, column):

    length = len(arr)
    output = [0 for x in range(length)]
    sortArr = [[0,0] for x in range(length)]

    for i in range(length):#extract values from column
        sortArr[i][0] = i
        sortArr[i][1] = arr[i][column]
    
    sortArr = mergeSortIndex(sortArr)

    for j in range(length):
        index = sortArr[j][0]
        output[j] = arr[index]
    
    return output

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
            rightCounter -= 1
    
    return output
