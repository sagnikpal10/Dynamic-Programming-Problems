def min_ops(s1,s2,n,m):

    if(n == 0):
        return m
    if(m == 0):
        return n
    
    if(s1[n-1] == s2[m-1]):
        return min_ops(s1,s2,n-1,m-1)
    else:
        a = min_ops(s1,s2,n-1,m-1) + 1
        b = min_ops(s1,s2,n-1,m) + 1
        c = min_ops(s1,s2,n,m-1) + 1
        return min(a,b,c)

print(min_ops("sunday","saturday",6,8))