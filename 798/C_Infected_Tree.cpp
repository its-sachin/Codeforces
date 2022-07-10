#include<bits/stdc++.h>

using namespace std;

//typedef long long int;
#define inf 1e18
#define mod 1000000007
#define pb push_back


int setc(int i, int* count, bool* vis, vector<int> *adj ){
    int c=0;
    vis[i-1]=true;
    for (int j : adj[i]){
        if(not vis[j-1])
            c+=setc(j, count,vis,adj);
    }
    count[i]=c;
    return c+1;
}

int ans(int i,int* count, vector<int> *adj ){
    vector<int> pos;
    for (int j : adj[i]){
        if(count[j]<count[i])
            pos.push_back(j);
    }
    if(pos.size()==2)
        return max(count[pos[0]]+ans(pos[1],count,adj),count[pos[1]]+ans(pos[0],count,adj));
    else if(pos.size()==1)
        return count[pos[0]];
    else return 0;
}

int main(int argc, char const *argv[])
{
    int T;
    cin>>T;
    
    for(int t=0; t<T; t++){
        int n;
        cin >>n;
        vector<int> adj[n+1];

        for(int i=0;i<n-1;i++){
            int u,v;
            cin >>u>>v;

            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        int count[n+1];
        bool vis[n+1];
        for(int i=0;i<n+1;i++)vis[i]=false;
        setc(1,count,vis,adj);
        cout<<ans(1,count,adj)<<endl;
    }
    
    return 0;
}