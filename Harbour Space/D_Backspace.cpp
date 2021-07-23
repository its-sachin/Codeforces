#include<bits/stdc++.h>

using namespace std;

//typedef long long int;
#define inf 1e18
#define mod 1000000007
#define pb push_back



int main(int argc, char const *argv[])
{
    int T;
    cin>>T;
    
    for(int l=0; l<T; l++){
        string s;
        cin>>s;
        
        string t;
        cin>>t;
        
        int n = s.size();
        int m = t.size();

        if(m>n){
            cout<<"NO"<<endl;
            continue;
        }

        if(t=="" or s==t){
            cout<<"YES"<<endl;
            continue;
        }

        bool prev[m+1] = {0};
        bool curr[m+1] = {0};
        curr[0]=true;
        prev[0]=true;

        for (int i=1;i<=n; i++){
            for (int j=1;j<=m; j++){
                int q = curr[j];
                if(s[i-1]==t[j-1])
                    curr[j] = prev[j-1];
                else{
                    if(i>=2)
                        curr[j] = prev[j];
                    else
                        curr[j] = false;
                }
                prev[j]=q;
            }
        }
        

        if(curr[m])
             cout<<"YES"<<endl;
        else
             cout<<"NO"<<endl;
    }
    return 0;
}