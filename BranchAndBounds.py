# hold item information
class Item:
  def __init__(self, id, weight, profit):
    self.id = id
    self.weight = weight
    self.profit = profit

# hold tree item information
class Node:
  def __init__(self, id, isTaken, weight, profit, upper, lower, left, right):
    self.id = id
    self.isTaken = isTaken
    self.weight = weight
    self.profit = profit
    self.upper = upper
    self.lower = lower
    self.left = None
    self.right = None

# keep track of all items considered
class Items:
  id = 1
  itemCount = 0
  items = []

  def getIdList(self, index):
    data = []

    for i in range(index,len(self.items)):
      data.append(self.items[i].id)

    return data

  def getWeightList(self, index):
    data = []

    for i in range(index,len(self.items)):
      data.append(self.items[i].weight)

    return data

  def getProfitList(self, index):
    data = []

    for i in range(index,len(self.items)):
      data.append(self.items[i].profit)

    return data

  def addItem(self, weight, profit):
    # create new item
    item = Item(self.id, weight, profit)

    # update id
    self.id+=1

    # update count
    self.itemCount+=1

    # add item to list
    self.items.append(item)

items = Items()

# CHANGE ME! capacity of knapsack
capacity = 19

# CHANGE ME! example item set
items.addItem(3,21)
items.addItem(6,30)
items.addItem(5,15)
items.addItem(10,20)
items.addItem(8,8)
	
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
  
 import pandas as pd

# perform greedy approach for all items from startIndex to last element
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
  df = df.sort_values(by='Ratio', ascending=False)

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
  
 def getBounds(strategy, items, id, weight):
  if(strategy == 1):
    return getStrategy1Bounds(items, id)
  elif(strategy == 2):
    return getStrategy2Bounds(items, id, weight)
  elif(strategy == 3):
    return getStrategy3Bounds(items, id, weight)
  else:
    print("Not a valid strategy. Please choose 1, 2, or 3")
    return None

# take all undecided items
def BranchAndBound(items, maxWeight, strategy=3):
  queue = []         # empty queue
  decisionCount = 1  # decision count
  pruneCount = 0     # total nodes pruned
  maxProfit = 0      # start max at 0

  # create dummy root
  root = Node(0,0,0,0,0,0,None, None)
  queue.append(root)

  # continue looping if nodes need to be processed
  while(len(queue)>0):
    # remove node from queue and potentially add children
    currentRoot = queue.pop(0)

    # only add children if there are more items to process
    if(currentRoot.id+1<=items.itemCount):
        ## TAKE ITEM ##
        # compute bounds if take next item
        upper = getBounds(strategy, items, currentRoot.id, maxWeight-currentRoot.weight)

        # new profit and weight and upper if we add item
        newProfit = currentRoot.profit + items.items[currentRoot.id].profit
        newWeight = currentRoot.weight + items.items[currentRoot.id].weight
        newUpper = currentRoot.profit + upper

        print("Decision: ", decisionCount,
              " . Consider item ", currentRoot.id,
              " for profit ", items.items[currentRoot.id].profit,
              " and weight ", items.items[currentRoot.id].weight,
              "? Current Max Profit: ", maxProfit,
              " Avilable Weight: ", maxWeight-currentRoot.weight,
              ", Upper: ", newUpper,
              ", Bound Prune?: ", newUpper <= maxProfit,
              ", Infeasibility Prune?: ", newWeight > maxWeight)
        
        decisionCount+=1

        # only check subtree of adding item if it passes bound check and infeasibility check
        if(newUpper > maxProfit and newWeight <= maxWeight):
          if(newProfit>maxProfit):
            maxProfit = newProfit

          # taking item
          root.left = Node(
            currentRoot.id+1, # ID
            1,                # is taken?
            newWeight,        # weight
            newProfit,        # profit
            0,                # lower
            newUpper,         # upper
            None,             # left child
            None              # right child
          )
          queue.append(root.left)
        
        # prune tree
        else:
          pruneCount+=((2**(items.itemCount-currentRoot.id-1))-1)
     

        ## DONT TAKE ITEM ##
        # compute bounds if dont take next item
        upper = getBounds(strategy, items, currentRoot.id+1, maxWeight-currentRoot.weight)

        # upper bound for current node
        newUpper = currentRoot.profit + upper

        print("Decision: ", decisionCount, 
              " . Don't take item ", currentRoot.id, 
              " for profit ", items.items[currentRoot.id].profit,
              " and weight ", items.items[currentRoot.id].weight,
              "? Current Max Profit: ", maxProfit,
              " Avilable Weight: ", maxWeight-currentRoot.weight,
              ", Upper: ", newUpper, 
              ", Bound Prune?: ", newUpper <= maxProfit, 
              ", Infeasibility Prune?: ", currentRoot.weight > maxWeight)
        
        decisionCount+=1

        # only check subtree of not adding item if it passes bound check and infeasbility check
        if(newUpper > maxProfit and currentRoot.weight <= maxWeight):

          # dont take next item
          root.right = Node(
              currentRoot.id+1,   # ID
              0,                  # is taken?
              currentRoot.weight, # weigt
              currentRoot.profit, # profit
              0,                  # lower bound
              newUpper,           # upper bound
              None,               # left child
              None                # right child
          )
          queue.append(root.right)
      
        # prune tree
        else:
          pruneCount+=((2**(items.itemCount-currentRoot.id-1))-1)

  print("Subtrees Pruned: ", pruneCount)
  print("Best Profit: ", maxProfit)
  
print("Strategy1")
BranchAndBound(items, maxWeight=capacity, strategy=1)

print("Strategy2")
BranchAndBound(items, maxWeight=capacity, strategy=1)

print("Strategy3")
BranchAndBound(items, maxWeight=capacity, strategy=1)
