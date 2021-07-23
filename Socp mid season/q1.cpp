#include<bits/stdc++.h>

using namespace std;

//typedef long long int;
#define inf 1e18
#define mod 1000000007
#define pb push_back

const int n = 1000000;
int largsq[n+1];

void SPF(){

    for (int i = 0; i <= n; i++){
    
        largsq[i]=1;
    }
    int i=4;
    int u=5;
    while(i<=n){
        int c = i;
        while(c<=n){
            largsq[c]=i;
            c+=i;
        }
        i+=u;
        u+=2;
    }
}

int main(int argc, char const *argv[])
{

    SPF();

    int T;
    cin>>T;
    
    for(int t=0; t<T; t++){
        int k;
        cin>>k;

        unordered_map<int,int> kis;

        int ans = 0;
        
        for(int i=0; i<k; i++){
            int ai;
            cin>>ai;

            int ki = ai/largsq[ai];
            if(kis.find(ki)==kis.end())
                kis[ki]=1;
            else
                kis[ki]+=1;

            ans=max(ans,kis[ki]);

        }

        cout<<ans<<endl;
    }
    return 0;
}