def getBounds(strategy, items, id, weight):
  if(strategy == 1):
    return getStrategy1Bounds(items, id)
  elif(strategy == 2):
    return getStrategy2Bounds(items, id, weight)
  else:
    return getStrategy3Bounds(items, id, weight)

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
              " for profit ", items.items[currentRoot.id].weight,
              "? Current Max Profit: ", maxProfit,
              " Avilable Weight: ", maxWeight-currentRoot.weight,
              ", Upper: ", newUpper,
              ", Bound Prune?: ", newUpper <= maxProfit,
              ", Infeasibility Prune?: ", newProfit > maxWeight)
        
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
        upper = getStrategy3Bounds(items, currentRoot.id+1, maxWeight-currentRoot.weight)

        # upper bound for current node
        newUpper = currentRoot.profit + upper

        print("Decision: ", decisionCount, 
              " . Don't take item ", currentRoot.id, 
              " for profit ", items.items[currentRoot.id].weight,
              "? Current Max Profit: ", maxProfit,
              " Avilable Weight: ", maxWeight-currentRoot.weight,
              ", Upper: ", newUpper, 
              ", Bound Prune?: ", newUpper <= maxProfit, 
              ", Infeasibility Prune?: ", currentRoot.weight > maxWeight)

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
