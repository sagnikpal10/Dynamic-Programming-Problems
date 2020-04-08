#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
 
long long int a[100007], n;
long long int dp[100007];
 
int main() {
    memset(a, 0, sizeof(a));
    cin >> n;
    for (int i = 0; i < n; i++) {
        int j;
        cin >> j;
        a[j]++;
    }
    dp[0] = 0;
    dp[1] = a[1]; // a[1]*1 = a[1]
    for (int i = 2; i <= 100000; i++) { // Finding optimal points until the ith number
        dp[i] = max(dp[i - 1], dp[i - 2] + i*a[i]);
    }
    cout << dp[100000];
    return 0;
}