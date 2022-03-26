class Item:
  def __init__(self, id, weight, profit):
    self.id = id
    self.weight = weight
    self.profit = profit
 

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
