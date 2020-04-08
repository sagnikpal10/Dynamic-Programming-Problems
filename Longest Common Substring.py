def lcs(s1, s2, n1, n2, ans):

    # Base Cases
    if(n1 == 0 or n2 == 0):
        return ans

    # Recurrance Relation
    if(s1[n1 - 1] == s2[n2 - 1]):
        return lcs(s1,s2,n1-1,n2-1, ans + 1)
    else:
        return max(ans, lcs(s1,s2,n1-1,n2, 0), lcs(s1,s2,n1,n2-1, 0))
    

def lcs_dp(s1, s2, n1, n2):

    dp = [ [0 for _ in range(n2+1)] for _ in range(n1+1) ]

    result = 0

    for i in range(n1+1):
        for j in range(n2+1):
            if(i == 0 or j == 0):
                dp[i][j] = 0
            elif(s1[i-1] == s2[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
                result = max(dp[i][j], result)
            else:
                dp[i][j] = 0

    return result

print(lcs("abcdxyz", "xyzabcd", 7, 7, 0))