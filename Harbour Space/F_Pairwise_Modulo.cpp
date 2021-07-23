#include<bits/stdc++.h>

using namespace std;

//typedef long long int;
#define inf 1e18
#define mod 1000000007
#define pb push_back



int main(int argc, char const *argv[])
{
    int n;
    cin>>n;
    
    long long int a[n];
    long long int dp[n];
    dp[0]=0;

    for(int i=0; i<n; i++){
        long long int ai;
        cin>>ai;
        a[i] = ai;

        if(i>0){
            long long int s = 0;
            for (int j = 0; j < i; j++){
            
                s+=a[j]%a[i];
                s+=a[i]%a[j];
            }

            dp[i] = dp[i-1]+s;
        }

    }

    for (int i = 0; i < n; i++){
    
        cout<<dp[i]<<" ";
    }
    cout<<""<<endl;
    return 0;
}