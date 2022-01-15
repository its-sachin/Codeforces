#include <iostream>

using namespace std;

int pf(int n){

    int c=0;

    while(n%2 == 0){
        c+=1;
        n = n/2;
    }

    int i=3;
    while(i*i<=n){

        while(n%i == 0){
            c+=1;
            n = n/i;
        }
        i+=2;
    }

    if (n>1){
        c+=1;
    }
    return c;

}

int main(int argc, char const *argv[])
{
    int n;
    cin>>n;

    for (int i=0; i<n; i++){
        int a,b,k;

        cin>>a>>b>>k;

        if(k==0 && a==b){
            cout<<"YES"<<endl;
        }

        else if (k==1){
            if (a!=b && (a%b==0 || b%a==0)){
                cout << "YES"<<endl;
            }
            else{
                cout << "NO"<<endl;
            }
        }
        else{
            int p = pf(a)+pf(b);

            if (k>p){
                cout << "NO"<<endl;
            }
            else{
                cout << "YES"<<endl;
            }
        }
    }

    
    return 0;
}
