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

# CHANGE ME
capacity = 19

# CHANGE ME
items.addItem(3,21)
items.addItem(6,30)
items.addItem(5,15)
items.addItem(10,20)
items.addItem(8,8)

# breadth first approach for brute force using queue
def BruteForce(items, maxWeight):
  queue = []

  # start max at 0
  maxProfit = 0

  # create dummy root
  root = Node(0,0,0,0,0,0,None, None)

  # add dummy root to queue
  queue.append(root)

  # continue looping if nodes need to be processed
  while(len(queue)>0):
    # remove node from queue and potentially add children
    currentRoot = queue.pop(0)

    # only add children if there are more items to process
    if(currentRoot.id+1<=items.itemCount):
      # take next item
      # print(currentRoot.id +1, " is taken. Profit: ", currentRoot.profit + items.items[currentRoot.id].profit, " Weight: ", currentRoot.weight + items.items[currentRoot.id].weight)
      root.left = Node(currentRoot.id+1, 1, currentRoot.weight + items.items[currentRoot.id].weight, currentRoot.profit + items.items[currentRoot.id].profit, 0,0,None, None)

      # dont take next item
      #print(currentRoot.id +1, " is not taken. Profit: ", currentRoot.profit, " Weight: ", currentRoot.weight)
      root.right = Node(currentRoot.id+1, 0, currentRoot.weight, currentRoot.profit, 0,0,None, None)

      # add children to queue
      queue.append(root.left)
      queue.append(root.right)

    # if at leaf level, find max profit
    if(currentRoot.id == items.itemCount and currentRoot.profit>maxProfit and currentRoot.weight<=maxWeight):
        maxProfit = currentRoot.profit

  print("Subtrees Pruned: ", 0)
  print("Best Profit: ", maxProfit)
  
print("Brute Force")
BruteForce(items, capacity)