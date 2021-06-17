#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <limits>
#include <unordered_map>

using namespace std;


class Vertex{

public:

    int val;
    int parent;

    int height;
    vector<int> childs;

};


class Tree{

public:

    int N;
    Vertex* vertices;
    unordered_map<int,unordered_map<int,int>> lcaVal;


    Tree(int n){
        N=n;
        vertices = new Vertex[n];
    }

    void setVal(int vertex, int v){
        vertices[vertex-1].val = v;
    }
    
    void setParent(int child, int parent){

        vertices[child-1].parent = parent;
        vertices[parent-1].childs.push_back(child);
    }
    
    void dfs(int cur, int prev)
    {
        depth[cur] = depth[prev] + 1;
        parent[cur][0] = prev;
        for (int i=0; i<tree[cur].size(); i++)
        {
            if (tree[cur][i] != prev)
                dfs(tree[cur][i], cur);
        }
    }
    
    // Dynamic Programming Sparse Matrix Approach
    // populating 2^i parent for each node
    // Time complexity : O(nlogn)
    void precomputeSparseMatrix(int n)
    {
        for (int i=1; i<level; i++)
        {
            for (int node = 1; node <= n; node++)
            {
                if (parent[node][i-1] != -1)
                    parent[node][i] =
                        parent[parent[node][i-1]][i-1];
            }
        }
    }
    
    // Returning the LCA of u and v
    // Time complexity : O(log n)
    int lca(int u, int v){
        if (vertices[v-1].height < vertices[u-1].height){
            int temp = v;
            v = u;
            u = temp;
        }
    
        int diff = vertices[v-1].height - vertices[u-1].height;
    
        for (int i=0; i<level; i++)
            if ((diff>>i)&1)
                v = parent[v][i];
    
        // now depth[u] == depth[v]
        if (u == v)
            return u;
    
        // Step 2 of the pseudocode
        for (int i=level-1; i>=0; i--)
            if (parent[u][i] != parent[v][i])
            {
                u = parent[u][i];
                v = parent[v][i];
            }
    
        return parent[u][0];
    }

    int getHeight(int vertex){
        return vertices[vertex-1].height;
    }

    int getVal(int vertex){
        return vertices[vertex-1].val;
    }

    int getParent(int vertex){
        return vertices[vertex-1].parent;
    }


    int getLCA(int i, int j){
        
        // auto it = lcaVal.find(i-1);
        // if (it != lcaVal.end() && it->second.find(j-1) != it->second.end()){
            
        //     auto itin = it->second.find(j-1);
        //     return vertices[itin->second-1].val;
        // }

        int l = lca(i,j);
        

        // if (it==lcaVal.end()){
        //     unordered_map<int,int> t1;
        //     t1.insert({j-1,l});
        //     lcaVal.insert({i-1,t1});
        // } 
        // else{
        //     it->second.insert({j-1,l});
        // }

        // it = lcaVal.find(j-1);

        // if (it==lcaVal.end()){
        //     unordered_map<int,int> t1;
        //     t1.insert({i-1,l});
        //     lcaVal.insert({j-1,t1});
        // } 
        // else{
        //     it->second.insert({i-1,l});
        // }

        return vertices[l-1].val;
    }

    
};

int getDiesease(Tree* body, vector<int>* Dm, int m, vector<int> Qp){

    int maxVal = numeric_limits<int>::min();
    int diesease;

    for (int i=0; i<m; i++) {

        int sum =0;

        for (int q : Qp){

            int maxIC = numeric_limits<int>::min();

            for (int d: Dm[i]){
                int currIC = body->getLCA(q,d);
                // cout<<currIC<<endl;
                if (currIC > maxIC){
                    maxIC = currIC;
                }
            }

            sum+=maxIC;

        }

        if (maxVal<sum){
            maxVal = sum;
            diesease = i;
        }

    }

    return diesease+1;
}


int main(int argc, char const *argv[])
{
    string infile = argv[1]; 
    ifstream input(infile);

    ofstream ans("ans.txt");
    string line;

    getline(input,line);
    int n = stoi(line);

    Tree* body = new Tree(n);

    getline(input,line);

    stringstream token(line);
    for (int i=2; i<=n; i++){
        int p;
        token>>p;
        body->setParent(i,p);
    }


    getline(input,line);
    token.clear();
    token.str(line);
    for (int i=1; i<=n; i++){
        int v;
        token>>v;
        body->setVal(i,v);
    }

    body->setHeight(1,0);
    

    getline(input,line);
    int m = stoi(line);

    vector<int> Dm[m];

    for (int i=0; i<m; i++) {

        getline(input,line);
        token.clear();
        token.str(line);

        int dm;
        token>>dm;

        for (int j=0; j<dm; j++){
            int v;
            token>>v;
            Dm[i].push_back(v);
        }
        
    }

    getline(input,line);
    int p = stoi(line);

    vector<int> Qp[p];

    for (int i=0; i<p; i++) {

        getline(input,line);
        token.clear();
        token.str(line);

        int qp;
        token>>qp;

        for (int j=0; j<qp; j++){
            int v;
            token>>v;
            Qp[i].push_back(v);
        }

    }

    // for (int i=1; i<=n; i++){
    //     for (int j=1;j<=n;j++){
    //         cout<<"lca of "<<i<<" "<<j<<" "<<body->lca(i,j)<<endl;
    //     }
    // }

    for (int i=0; i<p; i++) {
        cout<<"patient left "<<p-i<<endl;
        ans<<getDiesease(body,Dm,m,Qp[i])<<endl;
    }


    return 0;
}
