#include <iostream>

using namespace std;

bool f(int n,int a,int b){
    if(n<1)
        return false;
    if(n==1 or (n-1)%b==0)
        return true;
    if(a!=1){
        while(n%a==0){
            n=n/a;
        }
        if(n==1 or (n-1)%b==0)
            return true;

        while(true){
            n=n-b;
            if(n<1)
                return false;
            if(n%a==0)
                return f(n,a,b);
            
        }
    }
    return false;
}
    
    

int main(int argc, char const *argv[])
{
    int T;
    cin>>T;
    
    for(int t=0; t<T; t++){

        int n;
        cin>>n;
        int a;
        cin>>a;
        int b;
        cin>>b;

        if(f(n,a,b))
            cout<<"Yes"<<endl;
        else
            cout<<"No"<<endl;
           
    }
    return 0;
}