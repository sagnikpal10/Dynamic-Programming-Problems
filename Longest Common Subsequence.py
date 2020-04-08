def lcs(s1, s2, n1, n2):

    # Base Cases
    if(n1 == 0 or n2 == 0):
        return 0

    # Recurrance Relation
    if(s1[n1 - 1] == s2[n2 - 1]):
        return lcs(s1,s2,n1-1,n2-1) + 1
    else:
        return max(lcs(s1,s2,n1-1,n2), lcs(s1,s2,n1,n2-1))
    

def lcs_dp(s1, s2, n1, n2):

    dp = [ [0 for _ in range(n2+1)] for _ in range(n1+1) ]

    for i in range(n1+1):
        for j in range(n2+1):
            if(i == 0 or j == 0):
                dp[i][j] = 0
            elif(s1[i-1] == s2[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Printing the lcs
    i = n1
    j = n2
    s = ""
    while(i > 0 and j > 0):
        if(s1[i-1] == s2[j-1]):
            s = s1[i-1] + s
            i -= 1
            j -= 1
        else:
            if(dp[i-1][j] > dp[i][j-1]):
                i -= 1
            else:
                j -= 1
    print(s)

    return dp[n1][n2]

print(lcs_dp("AGGTAB", "GXTXAYB", 6, 7))










