import math

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
    initial = 0
    for j in range(period):
      initial += arr[j]
    output[0] = initial/period

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

# stdDev
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
  lnArr = [0 for x in range(total)]

  for i in range(total):
    lnArr[i] = math.log(arr[i+1]/arr[i])
  
  avgArr = fastSMA(lnArr, period, False)
  output = [[0,0] for x in range(len(avgArr))]

  index = (arr.index).tolist()
  for i in range(len(avgArr)):
    output[i][0] = index[i + period]

  for i in range(len(avgArr)):
    sumSD = 0
    
    for j in range(period):
      mean = avgArr[i]
      sumSD += (lnArr[i+j] - mean) ** 2
    
    output[i][1] = math.sqrt(sumSD / period)
  
  return output

# MACD - 12EMA, 26EMA, MACD(12EMA - 26EMA), Signal(9EMA of MACD), Histogram(MACD - Signal)
def MACD(arr, a = 12, b = 26, c = 9):#no point in asking dateAdd, this is strictly for financial analysis
  fastArr = EMA(arr, a, False)
  slowArr = EMA(arr, b, False)
  total = len(slowArr)
  offset = len(fastArr) - total
  diffArr = [0 for x in range(total)]

  for i in range(total):
    #diffArr[i][0] = slowArr[i][0]
    diffArr[i] = fastArr[i + offset] - slowArr[i]

  sigArr = EMA(diffArr, c, False)
  total2 = len(sigArr)
  offset2 = len(diffArr) - total
  histArr = [0 for x in range(total2)]

  for j in range(total2):
    histArr[j] = diffArr[j + offset2] - sigArr[j]

  fastArr = dateArray(arr, fastArr)
  slowArr = dateArray(arr, slowArr)
  diffArr = dateArray(arr, diffArr)
  sigArr = dateArray(arr, sigArr)
  histArr = dateArray(arr, histArr)

  return [fastArr, slowArr, diffArr, sigArr, histArr]



#MUST INCLUDE CASE WHEN U HAVE ARRAY WITH DATES IN ITSELF# USE TRANSPOSE() from main.py

