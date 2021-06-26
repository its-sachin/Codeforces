#include <iostream>

using namespace std;

// bool palindrome(string s, int n){
//     int i=0;
//     int j=n-1;

//     while(i<j){
//         if (s[i]!=s[j]){
//             return false;
//         }
//         i+=1;
//         j-=1;
//     }
//     return true;
// }

bool patternj(string s, int n){
    if (n==1 || n==0){
        return true;
    }
    int l1 = 0;
    int r1 = n/2 -1;
    int l2 = (n+1)/2;
    int r2 = n-1;

    while(l1<r2){
        if ((l1<r1 && s[l1] != s[r1]) || (l2<r2 && s[l2] != s[r2]) || (s[l1] != s[r2])){
            return false;
        }
        l1+=1;
        r1-=1;
        l2+=1;
        r2-=1;
    }
    return true;
}

int main(int argc, char const *argv[])
{
    int t;
    cin>>t;

    for(int i=0; i<t; i++){
        string s;
        cin>>s;

        if (patternj(s,s.length())){
            cout<<"yes"<<endl;
        }
        else{
            cout<<"no"<<endl;
        }
    }
    return 0;
}
