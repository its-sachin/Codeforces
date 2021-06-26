#include <iostream>
#include <vector>
#include <limits>
#include <queue>
#include <unordered_map>

using namespace std;

class Tree{

private:
    long N;
    vector<pair<long, long>>* adj;

public:

    Tree(long n){
        N = n;
        adj = new vector<pair<long, long>>[n];

    }

    void addEdge(long u, long v, long wt){

        adj[u-1].push_back({v-1, wt});
        adj[v-1].push_back({u-1, wt});
    }


    void shortest(){
        long min = numeric_limits<long>::max();
        unordered_map<long,pair<long,long>> p={{0,{0,0}}};
        queue<long> qu;
        qu.push(0);
        int left = 1;
        
        while(left>0){
            cout<<left<<endl;
            left-=1;
            long node = qu.front();
            pair<long,long> curr = p.at(node);
            bool done = true;
            for (pair<long,long> child : adj[node]){
                if (p.find(child.first) == p.end()){
                    done = false;
                    if (min>curr.first+curr.second+child.second){
                        p[curr.first] = {curr.first+curr.second+child.second,curr.second+child.second};
                    }
                    qu.push(curr.first);
                    left+=1;
                }
            }
            if (!done && curr.first<min){
                min = curr.first;
            }

        }

        cout<<min<<endl;
        
    }

};

int main(int argc, char const *argv[])
{
    long t;
    cin>>t;

    for (long i=0; i<t; i++){
        long n;
        cin>>n;

        Tree *t = new Tree(n);


        for (long j=0; j<n-1; j++){
            long u,v;
            long w;
            cin>>u>>v>>w;

            t->addEdge(u,v,w);
        }
        t->shortest();
    }

    return 0;
}
