int maxVal(int* v, int* wt, int w, int index, int n){
    
    if(w<=0 || index==n) return 0;
    
    if(memo[index][w] != -1) return memo[index][w];
    
    if(wt[index] > w) return maxVal(v,wt,w,index+1,n);
    
    int q1 = maxVal(v,wt,w-wt[index],index+1,n) + v[index];
    int q2 = maxVal(v,wt,w,index+1,n);
    
    memo[index][w] = max(q1,q2);
    
    return memo[index][w];
}


int knapSack(int W, int wt[], int val[], int n) 
{ 
   int i, w; 
   int K[n+1][W+1]; 
  
   // Build table K[][] in bottom up manner 
   for (i = 0; i <= n; i++) 
   { 
       for (w = 0; w <= W; w++) 
       { 
           if (i==0 || w==0) 
               K[i][w] = 0; 
           else if (wt[i-1] <= w) 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]); 
           else
                K[i][w] = K[i-1][w]; 
       } 
   } 
  
   return K[n][W]; 
} 