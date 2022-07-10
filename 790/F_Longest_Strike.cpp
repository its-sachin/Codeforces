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
        int n,k;
        cin >> n >> k;
        
        unordered_map<int,int> m;
        for(int i=0; i<n; i++){
            int ai;
            cin>>ai;
            if(m.find(ai) == m.end())m[ai]=1;
            else m[ai]+=1;
        }
        
        vector<int> a;
        for (auto i: m){
            a.push_back(i.first);
        }
        sort(a.begin(),a.end());

        vector<int> op;
        int i=0;
        n=a.size();
        while (i<n){
            if(m[a[i]]>=k){
                int j=i+1;
                while(j<n and a[j]==a[j-1]+1 and m[a[j]]>=k)j+=1;
                if(op.size()==0 or op[1]-op[0]<a[j-1]-a[i]){
                    op.clear();
                    op.push_back(a[i]);
                    op.push_back(a[j-1]);
                }
                i=j;
            }
            else i+=1;
        }

        if(op.size()==0)cout << -1 << endl ;
        else cout << op[0]  << " " <<op[1] << endl;
    }
    return 0;
}