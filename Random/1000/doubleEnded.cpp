#include <iostream>

using namespace std;


int lcsubs(string a, string b){
    int n = a.size();
    int m = b.size();

    int** dp = new int*[n+1];

    // here dp[i][j] represents length of common substring including a[i] and b[j]

    for(int i=0; i<=n; i++){
        dp[i] = new int[m+1];
        dp[i][0]=0;
    }
    for(int i=1; i<=m; i++){
        dp[0][i]=0;
    }

    int ma=0;
    for (int i=1; i<=n; i++){
        for (int j=1; j <=m; j++){
        
            if(a[i-1]==b[j-1]){
                dp[i][j] = 1+dp[i-1][j-1];
                ma = max(ma,dp[i][j]);
            }
            else{
                dp[i][j] = 0;
            }
            // cout<<i<<" "<<j<<endl;
            // print(dp,n,m);
        }
    }

    return ma;
}

int main(int argc, char const *argv[])
{
    int T;
    cin>>T;
    
    for(int t=0; t<T; t++){
        string a;
        cin>>a;

        string b;
        cin>>b;

        int l = lcsubs(a,b);
        int n = a.size();
        int m = b.size();

        cout<< (n-l+m-l)<<endl;   
    }
    return 0;
}