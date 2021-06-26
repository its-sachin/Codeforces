#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char const *argv[])
{
    int t;
    cin>>t;

    for (int o=0;o<t;o++){
        long n;
        cin>>n;

        long ar[n+1];
        ar[0]=0;
        for (long i=1; i<=n; i++){
            long k;
            cin>>k;
            ar[i]=k;
        }
        int c=0;

        for (long i=1; i<=n; i++){
            if(ar[i]!=0){
                long k = ceil((2*i+1)/ar[i]);
                cout<<"f "<<k<<" "<<i<<" "<<ar[i]<<endl;
                while(k*ar[i]-i<=n){
                    if(ar[k*ar[i]-i]==k){
                        c+=1;
                    }
                    k+=1;
                }
            }
        }
        cout<<c<<"\n"<<endl;
    }
    return 0;
}
