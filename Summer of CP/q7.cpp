#include <iostream>

using namespace std;

int nc2(int n){
    if (n<2){
        return 0;
    }
    return (n*(n-1))/2;
}

int main(int argc, char const *argv[])
{
    int t;
    cin>>t;

    for(int i=0; i<t; i++){
        int n;
        cin>>n;

        int e=0;

        for (int j=0; j<n; j++){
            int k;
            cin>>k;
            
            if ((k%8)%2==0){
                e+=1;
            }
        }
        int c = nc2(e)+nc2(n-e);
        cout<<c<<endl;
    }
}