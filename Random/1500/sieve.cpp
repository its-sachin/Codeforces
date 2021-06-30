#include <iostream>
using namespace std;

int* SPF(int n){
    int* spf = new int[n+1];
    for (int i=0; i<=n; i++){
        spf[i]=i;
    }
    int i=2;
    while(i*i<=n){
        if(spf[i]==i){
            int j=i*i;
            while(j<=n){
                spf[j]=i;
                j+=i;
            }
        }
        i+=1;
    }
    return spf;
}

int main(int argc, char const *argv[])
{
    int n = 1000000000;
    int* spf = SPF(n);
    for(int i=2;i<n+1;i++){
        if(spf[i]==i){
            cout<<i<<" ";
        }
    } 
    return 0;
}
