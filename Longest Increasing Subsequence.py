def lis(arr, end):
    if(end == 0):
        dp[end] = 1
        return 1
    else:
        max_length = 1
        for i in range(end):
            if(arr[end] > arr[i]):
                max_length = max(max_length, lis(arr,i) + 1)
        return max_length


def lis_dp(arr, n):
    dp = [ 0 for _ in range(n+1)]
    dp[0] = 1

    lis = 1
    for i in range(1,n+1):
        max_len = 1
        for j in range(0,i):
            if(arr[i] > arr[j]):
                max_len = max(max_len, dp[j]+1)
        dp[i] = max_len
        lis = max(lis, max_len)
    print(dp)
    return lis


print(lis_dp([3,4,-1,0,6,2,3,-9], 7)) 