import sys

# Matrix A[i] has dimension p[i-1] x p[i] 
# for i = 1..n 
def min_ops(matrix, i, j):
    if(i == j):
        return 0
    _min = sys.maxsize


    # place parenthesis at different places  
    # between first and last matrix,  
    # recursively calculate count of 
    # multiplications for each parenthesis 
    # placement and return the minimum count
    for k in range(i,j):
        temp = min_ops(matrix,i,k) + min_ops(matrix,k+1,j) + matrix[i-1]*matrix[k]*matrix[j]
        _min = min(_min, temp)
    return _min


def min_ops_dp(matrix, n):

    dp = [ [0 for _ in range(n)] for _ in range(n)]

    for length in range(0,n):
        for i in range(1,n-length):
            j = i + length
            dp[i][j] = sys.maxsize
            if(i == j):
                dp[i][j] = 0
            else:
                for k in range(i,j):
                    dp[i][j] = min(dp[i][k] + dp[k+1][j] + matrix[i-1]*matrix[k]*matrix[j], dp[i][j])
        print() 
    return dp[1][n-1]


arr = [1, 2, 3, 4, 3]; 
n = len(arr); 

# print("Minimum number of multiplications is ", min_ops(arr, 1, n-1)); 
print("Minimum number of multiplications is ", min_ops_dp(arr, n)); 
