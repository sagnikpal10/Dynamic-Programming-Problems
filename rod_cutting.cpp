// Rod Cutting Problem
#include <bits/stdc++.h>

using namespace std;

//Recursive Approach 
int maxProfit(int * arr, int length)
{
    if(length==0) return 0;
    
    int ans = 0;
    for(int i=1;i<=length;i++)
    {
        ans = max(ans, arr[i] + maxProfit(arr,length-i));
    }
    
    return ans;
}

//Top Down Approach 
//Recursive Approach 

int memo[100] = {};

int maxProfit1(int * arr, int length)
{
    if(length==0) return 0;
    
    if(memo[length]!=-1) return memo[length];
    int ans = 0;
    for(int i=1;i<=length;i++)
    {
        ans = max(ans, arr[i] + maxProfit(arr,length-i));
    }
    memo[length] = ans;
    
    return ans;
}

//Bottom Down Approach
int maxProfit2(int * arr, int length)
{
    int dp[100] = {};
    
    for(int len=1;len<=length;len++)
    {
        int ans;
        for(int cut=1;cut<=len;cut++)
        {
            ans = max(arr[cut]+dp[len-cut], ans);
        }
        dp[len] = ans;
    }
    
    return dp[length];
}


int main()
{
    int arr[] = {0,1,3,2,5};
    memset(memo,-1,sizeof memo);
    cout<<maxProfit(arr,4)<<endl;
    cout<<maxProfit1(arr,4)<<endl;
    cout<<maxProfit2(arr,4)<<endl;
    
    return 0;
}







