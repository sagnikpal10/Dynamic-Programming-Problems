def max_points(coins, start, end):

    if(start > end):
        return 0
    if(start == end):
        return coins[start]

    option_1 = min(max_points(coins, start + 1, end - 1), max_points(coins, start, end - 1)) + coins[end]
    option_2 = min(max_points(coins, start + 2, end), max_points(coins, start + 1, end - 1)) + coins[start]

    return max(option_1, option_2)


print(max_points([20, 30, 2, 2, 2, 10], 0, 5))