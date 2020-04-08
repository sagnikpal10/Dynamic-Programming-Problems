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


def lps(seq, i, j, ans): 
	# Base Case 1: If there is 
	# only 1 character 
	if (i == j): 
		return ans + 1

	# Base Case 2: If there are only 2 
	# characters and both are same 
	if (seq[i] == seq[j] and i + 1 == j): 
		return 2 + ans
	
	# If the first and last characters match 
	if (seq[i] == seq[j]): 
		return lps(seq, i + 1, j - 1, ans + 2)

	# If the first and last characters 
	# do not match 
	return max(ans, lps(seq, i, j - 1, 0), lps(seq, i + 1, j, 0)) 

print(lps("babcbabcbaccba", 0, 13, 0))
print(lcs_dp("babcbabcbaccba", "babcbabcbaccba"[::-1], 14, 14))