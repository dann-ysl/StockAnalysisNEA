import matplotlib.pyplot as plt
# splits 2x1 array into 2 1x1 arrays, plotting the 2nd column against 1st column
def plotxy(arr):
  length = len(arr)
  xArr = [0 for i in range(length)]
  yArr = [0 for i in range(length)]

  for j in range(length):
    xArr[j] = arr[j][0]
    yArr[j] = arr[j][1]

  plt.plot(xArr, yArr)

# if date-price pair, separates dates and prices into 2 lists, if 2 lists of dates and prices, remakes date-price pair
def transpose(arr):
    xlength = len(arr)
    ylength = len(arr[0])
    output = [[0 for x in range(xlength)] for y in range(ylength)]

    for i in range(xlength):

        for j in range(ylength):
            output[j][i] = arr[i][j]

    return output


