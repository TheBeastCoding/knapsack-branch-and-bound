# Files
File 1: branch and bound: runs different branch and bound strategies
File 2: brute foce: runs brute force approach to fractional knapsack

# About The Strategies
Several Branch and Bound Techniques for the 01 Knapsack Problem

Strategy 1: Upper Bound = Take all undecided items (regardless of capacity)

Strategy 2: Upper Bound = Take all undecided items if each individual item can fit (regardless if they all could fit together)

Strategy 3: Upper Bound = Fractional knapsack of all undecided items


# How to Run the code
1) Create an items object to hold all items
 - ex. items = Items() 
2) Edit Desired Capaicty of Knapsack
 - ex. capacity = 13
3) Add items to code with the "addItem" function with weight as 1st parameter and profit as 2nd parameter. Repeat until all desired knapsack items are added.
 - ex. items.addItem(weight=2, profit=40)
4) Call the function "BranchAndBound" with the item list as the 1st parameter, knapsack capacity as 2nd parameter, and the strategy for the 3rd parameter.
 - ex. strategy 1: BranchAndBound(items, maxWeight=capacity, strategy=1)
 - ex. strategy 2: BranchAndBound(items, maxWeight=capacity, strategy=2)
 - ex. strategy 3: BranchAndBound(items, maxWeight=capacity, strategy=3)

# Interpretting the Results
When considering exploring the children of a given node, the branch and bound strategy will decide whether to prune the subtree. There are 2 ways a subtree is pruned and the choice is visible as boolean decisions in each decision printout:
1) If the upper bound of a subtree yields a profit then the best possible profit
2) If the knapsack exceededs capacity after considering the weight when taking an item

Additionally, the total number of pruned nodes from the subtrees are printedout along with the best profit attained from this strategy (all strategies should print the same profit, but the number of pruned trees may differ because of the tighness of the upper bound)
