#include<bits/stdc++.h>

using namespace std;

//typedef long long int;
#define inf 1e18
#define mod 1000000007
#define pb push_back




int main(int argc, char const *argv[])
{
    int l,r;
    cin>>l>>r;

    int k1 = log2(l);
    int k2 = ceil(log2(r+1));

    int a[k2+1];
    int p1 = pow(2,k1-1);
    int p2 = pow(2,k2-1);
    memset(a,p2,sizeof(a));

    for (int i = 0; i <= k1; i++)
    {
        a[k2-i] -= p1;
    }

    for (int i = r+1; i < 2*p2; i++)
    {
        constexpr k = bitset<const(k2)>(i).to_string();
    }
    return 0;
}