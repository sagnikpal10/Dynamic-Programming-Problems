def max_points(coins, start, end):

    if(start > end):
        return 0
    if(start == end):
        return coins[start]

    option_1 = min(max_points(coins, start + 1, end - 1), max_points(coins, start, end - 1)) + coins[end]
    option_2 = min(max_points(coins, start + 2, end), max_points(coins, start + 1, end - 1)) + coins[start]

    return max(option_1, option_2)

def max_points_dp(coins, n):
    
    dp = [ [0 for _ in range(n)] for _ in range(n) ]
    for L in range(0,n):
        for i in range(0,n-L):
            j = i + L
            if(i==j):
                dp[i][j] = coins[i]
            else:
                x = 0
                y = 0
                z = 0
                if(i+1 > j-1):
                    x = 0
                else:
                    x = dp[i+1][j-1]
                if(i+2>j):
                    y = 0
                else:
                    y = dp[i+2][j]
                dp[i][j] = max(min(x, dp[i][j-1])+coins[j], min(y, x)+coins[i])
    
    return dp[0][n-1]
            

print(max_points([20, 30, 2, 2, 2, 10], 0, 5))
print(max_points_dp([20, 30, 2, 2, 2, 10], 6))