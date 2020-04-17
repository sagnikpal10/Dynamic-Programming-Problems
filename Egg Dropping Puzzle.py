import sys  
# Function to get minimum number of trials  
# needed in worst case with n eggs and k floors  
def eggDrop(n, k): 
  
    # If there are no floors, then no trials 
    # needed. OR if there is one floor, one 
    # trial needed. 
    if (k == 1 or k == 0): 
        return k 
  
    # We need k trials for one egg  
    # and k floors 
    if (n == 1): 
        return k 
  
    ans = sys.maxsize
    # Consider all droppings from 1st  
    # floor to kth floor and return  
    # the minimum of these values plus 1. 
    for x in range(1, k + 1): 
  
        res = max(eggDrop(n - 1, x - 1),  eggDrop(n, k - x)) + 1
        ans = min(res, ans) 
  
    return ans

# Function to get minimum number of trials needed in worst 
# case with n eggs and k floors 
def eggDrop_dp(n, k): 
    # A 2D table where entery eggFloor[i][j] will represent minimum 
    # number of trials needed for i eggs and j floors. 
    eggFloor = [[0 for x in range(k+1)] for x in range(n+1)] 

    for i in range(1, n+1): 
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0

    for j in range(1, k+1): 
        eggFloor[1][j] = j 
   
    for i in range(2, n+1): 
        for j in range(2, k+1): 
            eggFloor[i][j] = sys.maxsize 
            for x in range(1, j+1): 
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
                eggFloor[i][j] = min(eggFloor[i][j], res) 
  
    # eggFloor[n][k] holds the result 
    return eggFloor[n][k] 


n = 2
k = 10
print("Minimum number of trials in worst case with", n, "eggs and", k, "floors is", eggDrop(n, k)) 
print("Minimum number of trials in worst case with", n, "eggs and", k, "floors is", eggDrop_dp(n, k)) 







