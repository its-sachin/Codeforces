#include<bits/stdc++.h>

using namespace std;

//typedef long long int;
#define inf 1e18
#define mod 1000000007
#define pb push_back

int xorr(int a,int b,int k){
    int p=1;
    int ans=0;
    while(a>0 or b>0){
        ans+=((a%k - b%k + k)%k)*p;
        a/=k;
        b/=k;
        p*=k;
    }
    return ans;
}

int main(int argc, char const *argv[])
{
    int T;
    cin>>T;
    
    for(int t=0; t<T; t++){
        int n;
        cin>>n;
        
        int k;
        cin>>k;
        
        
        int done =0;
        int i=0;
        while(done==0){
            if(i==0)
                cout<<0<<endl;
            else{
                if(i%2==0)
                    cout<<xorr(i,i-1,k)<<endl;
                else
                    cout<<xorr(i-1,i,k)<<endl;
            }
            cin>>done ;
            cout.flush();
            i+=1;
        }
    }
    return 0;
}