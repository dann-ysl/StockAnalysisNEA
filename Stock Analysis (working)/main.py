import indicators as ind
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import os

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

### API
today = dt.datetime.today()
start = today + dt.timedelta(-100)##to be user input
end = today
df = web.DataReader("TSLA", "yahoo", start, end)
stock2 = df["Close"] #extracts only 'Close'

MACDFull = ind.MACD(stock2)
EMA12Arr = MACDFull[0]
EMA26Arr = MACDFull[1]
MACDArr = MACDFull[2]
Signal = MACDFull[3]
Histogram = MACDFull[4]

newArr = transpose(MACDArr)
sigArr = transpose(Signal)
Histogram = transpose(Histogram)

plt.plot(newArr[0], newArr[1], label="MACD")
plt.plot(sigArr[0], sigArr[1], label="Signal")
plt.plot(Histogram[0], Histogram[1], label="Histogram")
plt.legend()
#plt.plot(stock2)
plt.show()