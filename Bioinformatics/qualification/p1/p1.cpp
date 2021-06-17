#include <iostream>
#include <fstream>
#include <sstream>
#include <unordered_map>

using namespace std;

int main(int argc, char const *argv[])
{
    ifstream input("2.txt");

    ofstream ans("ans.txt");
    string line;

    getline(input,line);
    int t = stoi(line);

    for (int i=0; i<t; i++) {

        getline(input,line);
        stringstream cs(line);
        int n,l;
        cs>>n>>l;

        string a[n];
        for (int j=0; j<n; j++){

            getline(input,line);
            a[j]=line;
        }

        unordered_map<string,int> a1;
        int k=0;
        int index=1;
        while(k<l){
            string s="";
            for (int j=0; j<n; j++){
                s+=a[j].at(k);
            }

            if (a1.find(s) == a1.end()){
                a1.insert({s,index});
                index+=1;
            }
            k+=1;
        }

        ans<<a1.size()<<endl;

        k=0;
        while(k<l){
            string s="";
            for (int j=0; j<n; j++){
                s+=a[j].at(k);
            }

            ans<<a1.find(s)->second<<" ";
            k+=1;
        }

        
        ans<<""<<endl;
    }

    input.close();
    ans.close();
    return 0;
}
