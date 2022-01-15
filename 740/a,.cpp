#include <iostream>
#include <vector>
#include <cmath>
#include <math.h>
#include <set>
#include <unordered_map>
#include <map>
#include <queue>
#include <string>
#include <array>
#include <algorithm>
typedef long long ll;
using namespace std;
bool sorted(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] != i)
        {
            return 0;
        }
    }
    return 1;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int arr[n + 1];
        arr[0] = 0;
        for (int i = 1; i < n + 1; i++)
        {
            cin >> arr[i];
        }
        int iteration = 0;
        while (!sorted(arr, n + 1))
        {   
            iteration++;
            if (iteration % 2 != 0)
            {
                for (int i = 1; i <= n - 2;)
                {
                    if (arr[i] > arr[i + 1])
                    {
                        int temp = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = temp;
                    }
                    i = i + 2;
                }
            }
            else
            {
                for (int i = 2; i <= n - 1;)
                {
                    if (arr[i] > arr[i + 1])
                    {
                        int temp = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = temp;
                    }
                    i = i + 2;
                }
            }
        }
        cout << iteration << endl;
    }

    return 0;
}