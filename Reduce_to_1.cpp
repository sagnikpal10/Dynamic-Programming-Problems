#include <bits/stdc++.h>

using namespace std;

//Reduce a number to 1 by performing three types of operations in minimum number of steps
// 1. Divide by 3 (if divisible)
// 2. Divide by 2 (if divisible)
// 3. Substract 1
int cnt;

//Recursive solution
// This fubction returns the minimum no. of operations required to reduce n to 1
int reduce(int n)
{
    cnt++;
    if(n==1) return 0;
    
    int q1 = INT_MAX,q2 = INT_MAX,q3 = INT_MAX;
    if(n%3==0) q1 = 1 + reduce(n/3);
    if(n%2==0) q2 = 1 + reduce(n/2);
    q3 = 1 + reduce(n-1);
    
    return min(q1, min(q2,q3));
}

// Top down approach - Memoization
int memo[1000];

int reduce1(int n)
{
    cnt++;

    if(n == 1) return 0;
    
    if(memo[n] != -1) return memo[n];
    
    int q1 = INT_MAX,q2 = INT_MAX,q3 = INT_MAX;
    
    if(n%3==0) q1 = 1 + reduce(n/3);
    if(n%2==0) q2 = 1 + reduce(n/2);
    q3 = 1 + reduce(n-1);

    memo[n] = min(q1, min(q2,q3));
    return memo[n];
}

//Bottom Up approach
int reduce2(int n)
{
    int dp[1000] = {};
    dp[0] = 0;
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;
    
    
    for(int i=4;i<=n;i++)
    {
        int q1 = INT_MAX,q2 = INT_MAX,q3 = INT_MAX;
        
        if(i%3==0) q1 = 1 + dp[i/3];
        if(i%2==0) q2 = 1 + dp[i/2];
        q3 = 1 + dp[i-1];
    
        dp[i] = min(q1, min(q2,q3));
    }
    
    return dp[n];
}

int main()
{
    memset(memo,-1,sizeof memo);
    
    cnt = 0;
    int n = 10;
    cout<<reduce2(n)<<endl;
    // cout<<cnt<<endl;
    return 0;
}
