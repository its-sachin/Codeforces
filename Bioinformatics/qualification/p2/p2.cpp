#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
// #include <unordered_map>
#include <limits>

using namespace std;



int part(int** M, int left, int right) {

    int out = left-1;
    float pivot = M[right][0];
    
    for(int i=left; i< right; i++) {
        if (M[i][0] < pivot ) {
            out+= 1;

            // cout<<"before "<<M[out][0]<<" "<<M[out][1]<<endl;
            int* temp = M[out];
            M[out] = M[i];
            M[i] = temp;
            // cout<<"after "<<M[out][0]<<" "<<M[out][1]<<endl;
        }
    
    }
    out += 1;
    int* temp = M[right];
    M[right] = M[out];
    M[out] = temp;

    return out;
}

void sortC(int** M, int low, int high)
{

    if(low<high) {
        
        int pivot = part(M,low,high);

        sortC(M,low,pivot-1);
        sortC(M,pivot+1,high);
        
    }
}


int search(int** a, int n, int val){
 
    if (val <= a[0][0]){
        return 0;
    }
    if (val >= a[n - 1][0]){
        return n - 1;
    }

    int i = 0;
    int j = n ;
    int mid = 0;
    while (i < j){
        mid = (i + j)/2;
 
        if (a[mid][0] == val){
            return mid;
        }
 
        if (val < a[mid][0]) {

            if (mid > 0 and val > a[mid - 1][0]){

                if (val - a[mid - 1][0] >= a[mid][0] - val){
                    return mid;
                }
                else{
                    return mid - 1;
                }
            }

            j = mid;
        }
         
        else {

            if (mid < n - 1 and val < a[mid + 1][0]){

                if (val - a[mid][0] >= a[mid+1][0] - val){
                    return mid+1;
                }
                else{
                    return mid;
                }

            i = mid + 1;
            }
        }
         
    }
    return mid;
}

void strToArr(string str, int** a,int n){

    int i=0;
    string word = "";
    for (auto x : str) 
    {
        if (x == ' ')
        {
            a[i][0] = stof(word);
            a[i][1] = i+1;
            word = "";
            i+=1;
        }
        else {
            word = word + x;
        }
    }

    if (i<n){
        a[i][0] = stof(word);
        a[i][1] = i+1;
    }
} 

int main(int argc, char const *argv[])
{

    string infile = argv[1]; 
    ifstream input(infile);

    ofstream ans("ans.txt");
    string line;

    getline(input,line);
    int t = stoi(line);

    for (int i=0; i<t; i++) {
        // cout<<"testcase progress"<<float(i/t)*100<<endl;

        int m,k,n;

        getline(input,line);
        stringstream linecs(line);
        linecs>>m>>k>>n;

        int** meta = new int*[m];
        int** adduct = new int*[k];
        int** signal = new int*[n];

        for (int j=0;j<m;j++){
            meta[j] = new int[2];
        }

        for (int j=0;j<k;j++){
            adduct[j] = new int[2];
        }

        for (int j=0;j<n;j++){
            signal[j] = new int[2];
        }

        getline(input,line);
        strToArr(line,meta,m);

        getline(input,line);
        strToArr(line,adduct,k);

        getline(input,line);
        strToArr(line,signal,n);


        sortC(meta,0,m-1);

        for (int j=0;j<n;j++){

            // cout<<"progress"<<float(j/n)*100<<"\r";

            float val = signal[j][0];
            bool done = false;
            pair<int,int> minIn;
            int minS = numeric_limits<int>::max();
            for (int ki=0; ki<k;ki++){

                float kv = meta[ki][0];
                int searched = search(meta,m,val-kv);

                if (searched != -1){

                    if (meta[searched][0] == val-kv){
                        ans<<meta[searched][1]<<" "<<adduct[ki][1]<<endl;
                        done =true;
                        break;
                    }
                    if ((kv+meta[searched][0])>0 && minS>abs(val-kv-meta[searched][0])){
                        minIn = {searched,ki};
                        minS = abs(val-kv-meta[searched][0]);
                    }

                }

            }
            if (!done){
                ans<<meta[minIn.first][1]<<" "<<adduct[minIn.second][1]<<endl;
            }
        }
        
    }

    input.close();
    ans.close();
    return 0;
}
