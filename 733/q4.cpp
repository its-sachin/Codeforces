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

        unordered_map<int,bool> val;
        unordered_map<int,bool> nd;
        unordered_map<int,bool> na;
        int ans[n];

        for (int i = 1; i <=n; i++){
        
            nd.insert({i,true});
            na.insert({i,true});
        }
        
        int a[n];
        for(int i=0; i<n; i++){
            int ai;
            cin>>ai;
            a[i] = ai;
            if(val.find(a[i])==val.end()){
                val[a[i]]=i+1;
                nd.erase(nd.find(i+1));
                na.erase(na.find(a[i]));
                ans[i]=a[i];
            }
        }

        cout<<n-na.size()<<endl;

        for(auto& i: nd){
            bool done =false;
            for (auto& j:na){
                if(i.first!=j.first){
                    ans[i.first-1]=j.first;
                    na.erase(na.find(j.first));
                    done =true;
                    break;
                }
            }
            if(!done){
                if(nd.size()!=1){
                    for (auto& k: nd){
                        if(k.first!=i.first){
                            ans[i.first-1]=ans[k.first-1];
                            ans[k.first-1]=i.first;
                            break;
                        }
                    }
                }
                else{
                    ans[i.first-1]=a[i.first-1];
                    ans[val[a[i.first-1]]-1]=i.first;
                }
            }
        }

        for (int i = 0; i < n; i++){
        
            cout<<ans[i]<<" ";
        }
        cout<<""<<endl;
    }
    return 0;
}