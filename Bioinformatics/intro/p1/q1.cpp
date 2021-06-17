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
        
        std::stringstream  lineStream(line);

        int a,b;
        lineStream>>a>>b;

        ans<<a+b<<endl;

    }

    input.close();
    ans.close();
    return 0;
}
