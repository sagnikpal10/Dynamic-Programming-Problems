n = int(input())

l = list(map(int, input().split()))

N = max(l)

d = {}
for x in l:
    d.setdefault(x,0)
    d[x] += 1

dp = [ 0 for _ in range(N+1) ]

dp[0] = 0
dp[1] = d[1]
if(N >= 2):
    for i in range(2,N+1):
        dp[i] = max(dp[i-1], dp[i-2] + d[i]*i)
    
print(dp[N])