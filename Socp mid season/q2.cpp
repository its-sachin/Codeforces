#include<bits/stdc++.h>

using namespace std;

#define lint long long int
#define inf 1e18
#define mod 1000000007
#define pb push_back
#define n 100001

lint power(lint x, lint y)
{
    lint ans = 1; 
    x = x%mod;
  
    if (x==0) 
        return 0;
 
    while (y>0){
        if (y&1)
            ans = (ans*x)%mod;
 
        y = y>>1;
        x = (x*x)%mod;
    }
    return ans;
}

int main(int argc, char const *argv[])
{
    lint t,k;
    cin>>t>>k;

    lint dp[n]={0};
    lint ans[n];

    dp[0]=0;
    ans[0]=0;

    for(lint i=1;i<k;i++){
        dp[i] = power(2,i);
        ans[i]=(ans[i-1]+dp[i])%mod;
    }

    dp[k] = (power(2,k)+power(26,k))%mod;
    ans[k]=(ans[k-1]+dp[k])%mod;

    lint done = k;

    for(lint j=0; j<t; j++){
        lint l1,l2;
        cin>>l1>>l2;

        if(l2>done){
            for (lint i=done+1;i<=l2;i++){
                if(dp[i]==0){
                    dp[i] = ((2*dp[i-1])%mod + (dp[i-k]*power(26,k))%mod)%mod;
                    ans[i] = (ans[i-1]+dp[i])%mod;
                }
            }
            done=l2;
        }

        cout<<(ans[l2]-ans[l1-1]+mod)%mod<<endl;
    }


    return 0;
}