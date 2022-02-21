import math
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Simple Moving Average (SMA) - Calculates an average over last 'period' amount of days, and repeats it for the series of dates inputted. O(n^2)
def SMA(arr, period):#hasn't been changed for 1st column: dates
  length = len(arr)
  if length >= period:
    
    total = length - period + 1
    output = [0 for x in range(total)]
  
    for i in range(total):
      initial = 0
      
      for j in range(period):
        initial += arr[i + j]
      
      output[i] = initial/period
  
    return output
  else:
    print ("Unable to calculate SMA")

# fastSMA, quicker version of SMA by removing nested 'for' loops. O(n)
def fastSMA(arr, period, dateAdd):
  length = len(arr)

  if length >= period:
    total = length - period + 1
    output = [0 for x in range(total)]

    #extract index of dates from API dataframe, then input these dates into 1st column
    #index = (arr.index).tolist()
    #for i in range(total):
        #output[i][0] = index[i + period - 1]

    #calculate first rngTotal, and hence first SMA value
    rngTotal = 0
    for j in range(period):
      rngTotal += arr[j]
    output[0] = rngTotal/period
    
    #calculate rngTotal, and hence corresponding SMA value
    for k in range(total - 1):
      rngTotal += arr[period + k] - arr[k]
      output[k+1] = rngTotal/period

    if dateAdd == True:
      return (dateArray(arr, output))
    else:
      return output

  else:
    print ("Unable to calculate SMA")

# Exponential Moving Average (EMA) - Same as SMA, but instead is a weighted average method, with more recent days receiving higher weights
def EMA(arr, period, dateAdd):
  length = len(arr)

  if length >= period:
    total = length - period + 1
    output = [0 for x in range(total)]
    
    #extract index of dates from API dataframe, then input these dates into 1st column
    #index = (arr.index).tolist()
    #for i in range(total):
        #output[i][0] = index[i + period - 1]
    
    #internal SMA: instead of calling SMA()[0] (which takes a long time as it calculates the whole array) we do 1 single calculation of the average
    total = 0
    for j in range(period):
      total += arr[j]
    output[0] = total/period

    #actual calculation
    c = 2/(period + 1)
    for k in range(total - 1):
      #EMAtoday = PRICEtoday*C + EMAyesterday*(1-C)
      output[k + 1] = (arr[period + k]*c) + ((output[k])*(1-c))

    if dateAdd == True:
      return (dateArray(arr, output))
    else:
      return output

  else:
    print ("Unable to calculate EMA")

# Standard Deviation (stdDev) - Measures how far prices deviate compared to its mean
def slowStdDev(arr, period, dateAdd):#absolutely useless, use volatility instead
  length = len(arr)
  if length >= period:
    total = length - period + 1

    if dateAdd == False:
      avgArr = fastSMA(arr, period, False)
      output = [0 for x in range(total)]

      for i in range(total):
        sumSD = 0
        
        for j in range(period):
          mean = avgArr[i]
          sumSD += (arr[i+j] - mean) ** 2
        
        output[i] = math.sqrt(sumSD / period)

    else:
      avgArr = fastSMA(arr, period, True)
      output = [[0,0] for x in range(total)]

      for i in range(total):
        sumSD = 0
        
        for j in range(period):
          mean = avgArr[i][1]
          sumSD += (arr[i+j] - mean) ** 2
        
        output[i][0] = avgArr[i][0]
        output[i][1] = math.sqrt(sumSD / period)
    
    return output

  else:
    print("Unable to calculate standard deviation")

# FDstdDev
def stdDev(arr, period, dateAdd):#absolutely useless, use volatility instead
  length = len(arr)
  if length >= period:
    avgArr = fastSMA(arr, period, False)
    total = length - period + 1
    output = [0 for x in range(total)]

    for i in range(total):
      sumSD = 0
      
      for j in range(period):
        mean = avgArr[i]
        sumSD += (arr[i+j] - mean) ** 2
      
      output[i] = math.sqrt(sumSD / period)
    
    if dateAdd == True:
      return (dateArray(arr, output))
    else:
      return output

  else:
    print("Unable to calculate standard deviation")

# add dates to 1D arrays (used by SMA and EMA), takes responsibility of adding dates, so SMA and EMA can output 1D (without date) or 2D (with date) arrays
def dateArray(orgArr, outArr):#orgArr: original array, outArr: output array
  output = [[0,0] for x in range(len(outArr))]
  offset = len(orgArr) - len(outArr)
  index = (orgArr.index).tolist()

  for i in range(len(outArr)):
    output[i][0] = index[i + offset]
    output[i][1] = outArr[i]
  
  return output

# Volatility or Standard Deviation of logaritmic returns
def volatility(arr, period, dateAdd):
  total = len(arr) - 1
  output = [0 for x in range(total)]

  for i in range(total):
    output[i] = math.log(arr[i+1]/arr[i])
  
  sdArr = stdDev(output, period, False)
  if dateAdd == True:
    return (dateArray(arr, sdArr))
  else:
    return sdArr

# Volatility or Standard Deviation of logaritmic returns
def slowVolatility(arr, period):
  total = len(arr) - 1
  output = [0 for x in range(total)]

  for i in range(total):
    output[i] = math.log(arr[i+1]/arr[i])
  
  avgArr = fastSMA(output, period, False)
  output1 = [[0,0] for x in range(len(avgArr))]

  index = (arr.index).tolist()
  for i in range(len(avgArr)):
    output1[i][0] = index[i + period]

  for i in range(len(avgArr)):
    sumSD = 0
    
    for j in range(period):
      mean = avgArr[i]
      sumSD += (output[i+j] - mean) ** 2
    
    output1[i][1] = math.sqrt(sumSD / period)
  
  return output1
  
#splits 2x1 array into 2 1x1 arrays, plotting the 2nd column against 1st column
def plotxy(arr):
  length = len(arr)
  xArr = [0 for i in range(length)]
  yArr = [0 for i in range(length)]

  for j in range(length):
    xArr[j] = arr[j][0]
    yArr[j] = arr[j][1]

  plt.plot(xArr, yArr)

stock = [1,2,3,4,5,6,7,8,9,10]
print (fastSMA(stock,5,False))

###API
today = dt.datetime.today()
start = today + dt.timedelta(-30)
end = today
df = web.DataReader("TSLA", "yahoo", start, end)
stock2 = df["Close"] #extracts only 'Close'

print (volatility(stock2,5,True))
print (slowVolatility(stock2,5))

#print (fastSMA(stock2,5,True))
#print (fastSMA(stock2,5,False))
#plotxy(fastSMA(stock2,5,True))
#plotxy(oldFastSMA(stock2,5))
#plt.plot(stock2)
#plt.show()
