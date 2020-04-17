import sys

def min_ops(matrix, i, j):
    if(i == j):
        return 0
    _min = sys.maxsize

    for k in range(i,j):
        temp = min_ops(matrix,i,k) + min_ops(matrix,k+1,j) + matrix[i-1]*matrix[k]*matrix[j]
        _min = min(_min, temp)
    return _min

arr = [1, 2, 3, 4, 3]; 
n = len(arr); 
  
print("Minimum number of multiplications is ", 
                min_ops(arr, 1, n-1)); 
