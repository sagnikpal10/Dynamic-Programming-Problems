def lcs_dp(s1, s2, n1, n2):

    dp = [ [0 for _ in range(n2+1)] for _ in range(n1+1) ]
    result = 0
    for i in range(n1+1):
        for j in range(n2+1):
            if(i == 0 or j == 0):
                dp[i][j] = 0
            elif(s1[i-1] == s2[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0

    return result

print(lcs_dp("forgeeksskeegfor", "forgeeksskeegfor"[::-1], 16, 16))