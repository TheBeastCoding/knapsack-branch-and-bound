import pandas as pd

# get all undecided items
def getStrategy1Bounds(items, startIndex):
  # sum all potential profits from undecided
  profit = sum(items.getProfitList(startIndex))
  return profit

# get all undecided items that can fit
def getStrategy2Bounds(items, startIndex, currentCapactiy):
  # take all undecided items
  sum = 0
  profitList = items.getProfitList(startIndex)
  weightList = items.getWeightList(startIndex)

  # add profits of those that can fit
  for itemIndex in range(0, len(weightList)):
    if(weightList[itemIndex]<=currentCapactiy):
      sum+=profitList[itemIndex]

  return sum

# perform greedy approach for all items from startIndex to last element using fractional knapsack
def getStrategy3Bounds(items, startIndex, maxWeight):
  # get item data
  idList = items.getIdList(startIndex)
  weightList = items.getWeightList(startIndex)
  profitList = items.getProfitList(startIndex)

  # create table with item data
  data = {'ID': idList, 'Weight': weightList, 'Profit': profitList}
  df = pd.DataFrame(data)

  # create column of item profit to weight ratio
  df['Ratio'] = df['Profit']/df['Weight']

  # sort descending by ratio
  df.sort_values(by=['Ratio'], ascending=False)

  # algorithm data
  availableWeight = maxWeight
  upperBoundProfit = 0

  # add as much of item as possible sequentially
  for index, row in df.iterrows():
    if(availableWeight>0):
      # get the most amount of weight from the item possible
      w = min(availableWeight, row['Weight'])

      # find how much profit I can get with w amount of the item
      upperBoundProfit+= w*row['Ratio']

      # udpate available weight after taking item
      availableWeight-=w

    else:
      break

  return upperBoundProfit
  
