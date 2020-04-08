def lps(seq, i, j): 
	# Base Case 1: If there is 
	# only 1 character 
	if (i == j): 
		return 1

	# Base Case 2: If there are only 2 
	# characters and both are same 
	if (seq[i] == seq[j] and i + 1 == j): 
		return 2
	
	# If the first and last characters match 
	if (seq[i] == seq[j]): 
		return lps(seq, i + 1, j - 1) + 2

	# If the first and last characters 
	# do not match 
	return max(lps(seq, i, j - 1), lps(seq, i + 1, j)) 

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

    return dp[n1][n2]

print(lps("GEEKSFORGEEKS", 0, 12))