//Wine Problem 2D - DP

#include <bits/stdc++.h>

using namespace std;

//Recursive Solution
int maxProfit(int * arr, int be, int en, int year)
{
    if(be>en) return 0;
    
    int q1 = arr[be]*year + maxProfit(arr,be+1,en,year + 1);
    int q2 = arr[en]*year + maxProfit(arr,be,en-1,year + 1);
    
    return max(q1,q2);
}

//Using Memoization Top Down approach

int memo[100][100];

int maxProfit2(int * arr, int be, int en, int year)
{
    if(be>en) return 0;
    
    if(memo[be][en] != -1) return memo[be][en];
    
    int q1 = arr[be]*year + maxProfit(arr,be+1,en,year + 1);
    int q2 = arr[en]*year + maxProfit(arr,be,en-1,year + 1);
    memo[be][en] = max(q1,q2);
    
    return memo[be][en];
}


// Using 2D DP
int maxProfit3(int * arr, int n)
{
    int dp[100][100];
    int year = n;
    
    //When year = n
    for(int i=0;i<n;i++)
    {
        dp[i][i] = year*arr[i];
    }
    //When year is n - 1
    year-=1;
    
    for(int len=2;len<=n;len++)
    {
        //Sliding window Technique
        for(int start = 0;start<=n-len;start++)
        {
            int endIndex = start + len - 1;
            dp[start][endIndex] = max( 
                                        arr[start]*year + dp[start + 1][endIndex],
                                        arr[endIndex]*year + dp[start][endIndex - 1]    
                                     );
        }
        year--;
    }
    
    return dp[0][n-1];
}

int main()
{
    int arr[] = {1, 4, 2, 3};
    memset(memo, -1, sizeof memo);
    cout<<maxProfit(arr,0,3,1)<<endl;
    cout<<maxProfit2(arr,0,3,1)<<endl;
    cout<<maxProfit3(arr, 4)<<endl;
    
    return 0;
}







