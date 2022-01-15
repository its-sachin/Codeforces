#include <iostream>
#include <vector>
#include<bits/stdc++.h>

using namespace std;

class Vertex{

public:
    //parent is index of parent (p-1 compare to actual one)
    int ai;
    int parent = -1;
    bool isCycle = false;

};

class Graph{

public:

    int N;
    Vertex* vertices;
    int k=0;


    Graph(int n){
        N=n;
        vertices = new Vertex[n];
    }

    void set(int i, int ai){
        vertices[i-1].ai = ai;
        if (ai+i-1<N && ai+i-1>=0){
            vertices[i-1].parent = ai+i-1;
        }
    }

    bool isCyclicUtil(int v, bool visited[], bool *recStack)
    {
        if(visited[v] == false){
            visited[v] = true;
            recStack[v] = true;

            int i = vertices[v].parent;

                if (i!=-1){

                if ( !visited[i] && isCyclicUtil(i, visited, recStack) ){
                    vertices[i].isCycle = true;
                    k+=1;
                    return true;
                }
                else if (recStack[i]){
                    vertices[i].isCycle = true;
                    k+=1;
                    return true;
                }
            }
    
        }
        recStack[v] = false;
        return false;
    }
    

    bool isCyclic()
    {

        bool *visited = new bool[N];
        bool *recStack = new bool[N];
        for(int i = 0; i < N; i++)
        {
            visited[i] = false;
            recStack[i] = false;
        }
    
        for(int i = 0; i < N; i++)
            if (isCyclicUtil(i, visited, recStack))
                return true;
    
        return false;
    }

    void print(){
        bool t = isCyclic();
        for (int i=0; i<N; i++){
            if (!vertices[i].isCycle){
                cout<<i+1<<" ";
            }
        }
        cout<<""<<endl;
    }

};

int main(int argc, char const *argv[])
{

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int t;
    cin>>t;

    for (int u=0; u<t; u++){
        int n;
        cin>>n;

        int a[n];

        for (int q=0; q<n; q++){
            int t;
            cin>>t;
            a[q] = t;
        }
        int b[n] = {0};

        int i=0; 
        int c=0;

        while(i<n){
            if (b[i] == 0){
                int j = i+a[i];
                vector<int> l;
                l.push_back(i);
                while(true){
                    if ((j>=n || j<0) || b[j]==1){
                        for (int k: l){
                            b[k] = 1;
                            c+=1;
                        }
                        break;
                    }

                    else if (b[j]==-1 || (find(l.begin(), l.end(), j) != l.end())){

                        for (int k: l){
                            b[k] = -1;
                        }
                        break;

                    }
                    l.push_back(j);
                    j=j+a[j];
                    
                }
            }
            i+=1;
        }

        cout<<c<<endl;
        for (int q=0; q<n; q++){
            if (b[q]==1){
                cout<<q+1<<" ";
            }
        }
        cout<<""<<endl;
    }
    return 0;
}
