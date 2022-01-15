#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, char const *argv[])
{
    ifstream input("input.txt");

    ofstream ans("ans.txt");
    string line;

    getline(input,line);
    int n = stoi(line);

    while(getline(input,line)){

        
        string s = line;

        getline(input,line);

        string t = line;

        int i=0;
        while(i<s.length()){
            if (s.at(i)== t.at(0)){
                int j=1;

                bool done = true;

                while(j<t.length()){

                    if ((i+j) >= s.length() || s.at(i+j) !=t.at(j)){
                        done=false;
                        break;
                    }
                    j+=1;
                }

                if (done){
                    ans<<i+1<<" ";
                }
            }
            i+=1;
        }
        ans<<""<<endl;
    }

    input.close();
    ans.close();
    return 0;
}
