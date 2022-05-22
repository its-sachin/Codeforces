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
    
    for(int t=0; t<T; t++){
        int n;
        cin>>n;

        string s;
        cin>>s;

        int k;
        cin >> k;

        unordered_map<char, bool> m;
        for(char c = 'a'; c<='z'; c++){
            m[c] = false;
        } 
        for(int i=0;i<k;i++){
            char d;
            cin >> d;
            m[d] = true;
        }
        
        k = n-1;
        int aa[n];
        memset(aa,0,sizeof(aa));
        for(int i=0; i<n; i++){
            if(m[s.at(n-i-1)]==true){
                aa[n-i-1]=abs(i-k);
                k=i;
            }
            
        }

        int l=0;
        int ans = 0;
        for(int i=0; i<n;i++){
            int v;
            if(l<=aa[i]){
                v=l;
                l=0;
            }
            else{
                v=aa[i];
                l-=aa[i];
            }
            ans = max(ans,v);
            l += 1;
        }
        cout << ans << endl;

        
    }
    return 0;
}